# Đây là File để tự động thêm Tags, xóa đuôi .md

import os
import re

# ==========================================
# PHẦN CẤU HÌNH (BẠN CÓ THỂ THAY ĐỔI Ở ĐÂY)
# ==========================================
folder_path = r"C:\Users\lptue\Desktop\WuFort\content\writeup\hutechctf"

# NOTE: THAY ĐỔI TAGS Ở ĐÂY. 
# Nếu bạn làm thư mục khác, ví dụ muốn đổi thành PicoCTF_Easy, chỉ cần sửa chữ "PicoCTF_Medium" bên dưới.
# Nhớ giữ nguyên cấu trúc 'tags: ["..."]'
tag_to_insert = 'tags: ["HuTechCTF"]' 
# ==========================================

for filename in os.listdir(folder_path):
    if not filename.endswith(".md"):
        continue

    filepath = os.path.join(folder_path, filename)

    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    # 1. Xóa đuôi .md ở dòng title (xử lý được cả trường hợp có hoặc không có ngoặc nháy)
    content = re.sub(r"^(title:.*?)\.md(.*)$", r"\1\2", content, flags=re.MULTILINE)

    # 2. Xử lý dòng tags
    if re.search(r"^tags:\s*\[.*\]\s*$", content, flags=re.MULTILINE):
        # Thay thế dòng tags cũ bằng nội dung biến tag_to_insert
        content = re.sub(r"^tags:\s*\[.*\]\s*$", tag_to_insert, content, flags=re.MULTILINE)
    else:
        # Nếu chưa có tags, chèn nội dung biến tag_to_insert ngay bên dưới dòng title
        content = re.sub(r"^(title:.*)$", rf'\1\n{tag_to_insert}', content, flags=re.MULTILINE)

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

print("Đã hoàn tất sửa lỗi title, cập nhật tags mới và đổi tên file!")