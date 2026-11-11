# Đây là file tự động đổi sang file tuyệt đối

import os
import re

# Thư mục chứa các bài viết
CONTENT_DIR = r"C:\Users\lptue\Desktop\WuFort\content"
# Đường dẫn tuyệt đối chuẩn tới thư mục ảnh trên LIVE SITE của ông
ABSOLUTE_PREFIX = "https://lptue.github.io/WuFort/images/"

def process_md_files():
    # Regex tìm markdown ảnh: ![alt](path) - Bỏ qua các ảnh đã có sẵn http/https
    pattern = re.compile(r'!\[(.*?)\]\((?!http|https)(.*?)\)')

    for root, dirs, files in os.walk(CONTENT_DIR):
        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                def replacer(match):
                    alt_text = match.group(1)
                    old_path = match.group(2)
                    
                    # Lấy tên file ảnh cuối cùng (ví dụ: từ "images/pic.png" hoặc "/pic.png" chỉ lấy "pic.png")
                    filename = os.path.basename(old_path)
                    
                    # Ghép thành link tuyệt đối chuẩn
                    new_url = ABSOLUTE_PREFIX + filename
                    return f'![{alt_text}]({new_url})'

                new_content = pattern.sub(replacer, content)
                
                # Chỉ ghi lại file nếu có sự thay đổi
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"[+] Đã cập nhật ảnh trong file: {filepath}")

if __name__ == "__main__":
    print("Bắt đầu quét và sửa link ảnh...")
    process_md_files()
    print("Hoàn tất!")