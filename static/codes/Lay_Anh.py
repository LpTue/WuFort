# Đây là file tự động lấy ảnh về

import os
import re
import sys
import time
import hashlib
import mimetypes
import html

from pathlib import Path
from urllib.parse import urlparse

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


# ==================================================
# CONFIGURATION
# ==================================================

# CONFIGURATION

PROJECT_DIR = Path(r"C:\Users\lptue\Desktop\WuFort")

CONTENT_DIR = PROJECT_DIR / "content"
IMAGE_DIR = PROJECT_DIR / "static" / "images"

IMAGE_PREFIX = "/images"

TOKEN = "25AOA19L65NPS59EJ1LOJRH1WEX6Z8GA2WACNQUBEOL7MFHAOT"

TIMEOUT = 30
REQUEST_DELAY = 0.3
BACKUP = False

# Chỉ tải ảnh từ HackMD, không gửi token đến domain khác.
ALLOWED_HOST = "hackmd.io"


# ==================================================
# REGEX
# ==================================================

MD_IMAGE_RE = re.compile(
    r'!\[(?P<alt>[^\]]*)\]'
    r'\((?P<body>(?:[^()]|\([^()]*\))*)\)'
)

URL_RE = re.compile(
    r'https?://[^\s<>"\'\]\)]+',
    re.IGNORECASE
)

HTML_IMAGE_RE = re.compile(
    r'<img\b[^>]*>',
    re.IGNORECASE
)

HTML_SRC_RE = re.compile(
    r'(\bsrc\s*=\s*)(["\'])(.*?)\2',
    re.IGNORECASE | re.DOTALL
)


# ==================================================
# STATISTICS
# ==================================================

stats = {
    "files": 0,
    "found": 0,
    "downloaded": 0,
    "existing": 0,
    "failed": 0,
    "external": 0
}

cache = {}
failed_urls = []


# ==================================================
# HTTP SESSION
# ==================================================

session = requests.Session()

session.headers.update({
    "Authorization": f"Bearer {TOKEN}",
    "User-Agent": "WuFort-Image-Migrator/2.0",
    "Accept": "image/*,*/*;q=0.8"
})

retry = Retry(
    total=3,
    connect=3,
    read=3,
    backoff_factor=0.7,
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["GET"],
    respect_retry_after_header=True
)

adapter = HTTPAdapter(max_retries=retry)

session.mount("https://", adapter)
session.mount("http://", adapter)


# ==================================================
# AUTHENTICATION
# ==================================================

def check_token():

    try:
        response = session.get(
            "https://api.hackmd.io/v1/me",
            timeout=TIMEOUT
        )

        if response.status_code == 200:
            return True

        if response.status_code == 401:
            print("[!] Token không hợp lệ hoặc đã hết hiệu lực.")
            return False

        print(f"[!] Không xác minh được token: HTTP {response.status_code}")
        return False

    except requests.RequestException as e:
        print(f"[!] Lỗi kết nối HackMD: {type(e).__name__}")
        return False


# ==================================================
# IMAGE VALIDATION
# ==================================================

def detect_extension(data, content_type, url):

    signatures = [
        (b"\x89PNG\r\n\x1a\n", ".png"),
        (b"\xff\xd8\xff", ".jpg"),
        (b"GIF87a", ".gif"),
        (b"GIF89a", ".gif"),
        (b"BM", ".bmp"),
        (b"\x00\x00\x01\x00", ".ico"),
        (b"II*\x00", ".tif"),
        (b"MM\x00*", ".tif")
    ]

    for signature, ext in signatures:
        if data.startswith(signature):
            return ext

    if len(data) >= 12:
        if data[:4] == b"RIFF" and data[8:12] == b"WEBP":
            return ".webp"

        if data[4:8] == b"ftyp":
            if data[8:12] in (b"avif", b"avis"):
                return ".avif"

    # SVG

    beginning = data[:4096].lstrip().lower()

    if b"<svg" in beginning:
        return ".svg"

    content_type = content_type.split(";")[0].strip().lower()

    mime_map = {
        "image/png": ".png",
        "image/jpeg": ".jpg",
        "image/gif": ".gif",
        "image/webp": ".webp",
        "image/svg+xml": ".svg",
        "image/bmp": ".bmp",
        "image/x-icon": ".ico",
        "image/tiff": ".tif",
        "image/avif": ".avif"
    }

    if content_type in mime_map:
        return mime_map[content_type]

    # Không nhận diện được thì không lưu.

    return None


# ==================================================
# URL VALIDATION
# ==================================================

def is_hackmd_image(url):

    try:
        parsed = urlparse(url)

        return (
            parsed.scheme == "https"
            and parsed.hostname == ALLOWED_HOST
            and parsed.path.startswith("/_uploads/")
        )

    except Exception:
        return False


# ==================================================
# IMAGE DOWNLOAD
# ==================================================

def download_image(url):

    url = html.unescape(url.strip())

    if url in cache:
        return cache[url]

    if not is_hackmd_image(url):
        stats["external"] += 1
        return None

    filename_hash = hashlib.sha256(
        url.encode("utf-8")
    ).hexdigest()[:24]

    # Kiểm tra ảnh đã tồn tại, không cần request lại.

    existing_files = list(
        IMAGE_DIR.glob(filename_hash + ".*")
    )

    if existing_files:
        filepath = existing_files[0]

        if filepath.stat().st_size > 0:

            local_url = f"{IMAGE_PREFIX}/{filepath.name}"

            cache[url] = local_url
            stats["existing"] += 1

            print(f"[=] {filepath.name} (đã tồn tại)")

            return local_url

    try:

        response = session.get(
            url,
            timeout=TIMEOUT,
            allow_redirects=True
        )

        response.raise_for_status()

        data = response.content

        content_type = response.headers.get(
            "Content-Type", ""
        )

        # Không chấp nhận trang HTML hoặc text lỗi.

        if content_type.lower().startswith(
            ("text/html", "text/plain")
        ):
            raise ValueError("Server trả về nội dung không phải ảnh")

        extension = detect_extension(
            data,
            content_type,
            response.url
        )

        if not extension:
            raise ValueError("Không nhận diện được định dạng ảnh")

        filename = filename_hash + extension

        filepath = IMAGE_DIR / filename

        # Ghi file an toàn.

        temp_path = IMAGE_DIR / (filename + ".tmp")

        try:
            with open(temp_path, "wb") as f:
                f.write(data)

            os.replace(temp_path, filepath)

        finally:
            if temp_path.exists():
                temp_path.unlink()

        local_url = f"{IMAGE_PREFIX}/{filename}"

        cache[url] = local_url
        stats["downloaded"] += 1

        print(f"[+] {filename}")

        time.sleep(REQUEST_DELAY)

        return local_url

    except requests.HTTPError as e:

        status = (
            e.response.status_code
            if e.response is not None
            else "HTTP Error"
        )

        reason = f"HTTP {status}"

    except requests.RequestException as e:

        reason = type(e).__name__

    except Exception as e:

        reason = str(e)

    cache[url] = None
    stats["failed"] += 1

    failed_urls.append(f"{url} | {reason}")

    filename = urlparse(url).path.split("/")[-1]

    print(f"[!] {filename} ({reason})")

    return None


# ==================================================
# MARKDOWN PROCESSING
# ==================================================

def process_markdown(content):

    def replace_markdown(match):

        alt = match.group("alt")
        body = match.group("body")

        urls = URL_RE.findall(body)

        if not urls:
            return match.group(0)

        # Hỗ trợ cả:
        # ![image](https://...)
        # ![image]([url](https://...))

        url = urls[-1]

        stats["found"] += 1

        local_url = download_image(url)

        if local_url:
            return f"![{alt}]({local_url})"

        return match.group(0)

    content = MD_IMAGE_RE.sub(
        replace_markdown,
        content
    )

    # HTML images

    def replace_html(match):

        tag = match.group(0)

        src_match = HTML_SRC_RE.search(tag)

        if not src_match:
            return tag

        url = html.unescape(src_match.group(3))

        if not url.lower().startswith(("http://", "https://")):
            return tag

        stats["found"] += 1

        local_url = download_image(url)

        if not local_url:
            return tag

        start, end = src_match.span(3)

        return (
            tag[:start]
            + local_url
            + tag[end:]
        )

    content = HTML_IMAGE_RE.sub(
        replace_html,
        content
    )

    return content


# ==================================================
# FILE PROCESSING
# ==================================================

def process_file(filepath):

    try:

        original = filepath.read_text(
            encoding="utf-8"
        )

        updated = process_markdown(original)

        if updated == original:
            return

        # Backup trước khi sửa.

        if BACKUP:

            backup_path = filepath.with_suffix(
                filepath.suffix + ".bak"
            )

            if not backup_path.exists():
                backup_path.write_text(
                    original,
                    encoding="utf-8"
                )

        temp_path = filepath.with_suffix(
            filepath.suffix + ".tmp"
        )

        temp_path.write_text(
            updated,
            encoding="utf-8",
            newline=""
        )

        os.replace(temp_path, filepath)

    except Exception as e:

        print(f"[!] Lỗi file {filepath.name}: {type(e).__name__}")


# ==================================================
# MAIN
# ==================================================

def main():

    print()
    print("=" * 48)
    print("       WUFORT - HACKMD IMAGE MIGRATOR")
    print("=" * 48)

    if not TOKEN:
        print("[!] Chưa thiết lập HACKMD_TOKEN.")
        return

    if not CONTENT_DIR.is_dir():
        print("[!] Không tìm thấy thư mục content.")
        return

    IMAGE_DIR.mkdir(parents=True, exist_ok=True)

    print("[*] Đang xác thực HackMD...")

    if not check_token():
        return

    print("[+] Xác thực thành công.")

    files = list(CONTENT_DIR.rglob("*.md"))

    stats["files"] = len(files)

    print(f"[*] Đang quét {len(files)} file Markdown...\n")

    for filepath in files:
        process_file(filepath)

    # Ghi danh sách ảnh lỗi.

    if failed_urls:

        failed_path = PROJECT_DIR / "failed_images.txt"

        failed_path.write_text(
            "\n".join(failed_urls),
            encoding="utf-8"
        )

    print()
    print("=" * 48)
    print("                  SUMMARY")
    print("=" * 48)

    print(f"Markdown scanned : {stats['files']}")
    print(f"Image references : {stats['found']}")
    print(f"Downloaded       : {stats['downloaded']}")
    print(f"Already existed  : {stats['existing']}")
    print(f"Failed           : {stats['failed']}")
    print(f"External skipped : {stats['external']}")

    print("-" * 48)

    if failed_urls:
        print("[!] Xem failed_images.txt để biết ảnh lỗi.")

    print("[+] Hoàn thành!")
    print("=" * 48)


if __name__ == "__main__":
    main()
