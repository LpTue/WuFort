import os
import re

folder_path = r"C:\Users\lptue\Desktop\WuFort\content\picoctf_medium"

for filename in os.listdir(folder_path):
    if not filename.endswith(".md"):
        continue

    filepath = os.path.join(folder_path, filename)

    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    # 1. Xóa đuôi .md ở dòng title (xử lý được cả trường hợp có hoặc không có ngoặc nháy)
    # Ví dụ: title: advanced-potion-making.md -> title: advanced-potion-making
    content = re.sub(r"^(title:.*?)\.md(.*)$", r"\1\2", content, flags=re.MULTILINE)

    # 2. Xử lý dòng tags
    # Nếu file đã có dòng tags (do code cũ chạy ra [\"...\"]), thì ghi đè lại cho chuẩn
    if re.search(r"^tags:\s*\[.*\]\s*$", content, flags=re.MULTILINE):
        content = re.sub(r"^tags:\s*\[.*\]\s*$", 'tags: ["PicoCTF_Medium"]', content, flags=re.MULTILINE)
    else:
        # Nếu chưa có, chèn tags: ["PicoCTF_Medium"] ngay bên dưới dòng title
        content = re.sub(r"^(title:.*)$", r'\1\ntags: ["PicoCTF_Medium"]', content, flags=re.MULTILINE)

    # Ghi lại nội dung vào file
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)

    # 3. Đổi tên file (Xóa _ ở đầu và .md.md thành .md)
    new_filename = filename
    if new_filename.endswith(".md.md"):
        new_filename = new_filename.replace(".md.md", ".md")
    
    if new_filename.startswith("_"):
        new_filename = new_filename[1:]

    new_filepath = os.path.join(folder_path, new_filename)

    # Thực hiện đổi tên file nếu tên có thay đổi
    if filepath != new_filepath:
        os.rename(filepath, new_filepath)

print("Đã hoàn tất sửa lỗi title, cập nhật tags và đổi tên file!")