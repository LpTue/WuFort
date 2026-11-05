---
title: Operation Oni
tags: ["PicoCTF_Medium"]
---

Tải bài tập tại [đây](https://learn.cylabacademy.org/library/284?page=1&category=4&difficulty=2&workspace=true&solved=true)

Ta tìm thấy file mã

![image](https://hackmd.io/_uploads/S1zvdy6hfl.png)

Ta trích xuất file dưới dạng `key_file`

![image](https://hackmd.io/_uploads/B1d3uJ6hMl.png)

![image](https://hackmd.io/_uploads/HkCmKJp2fg.png)

Theo log thì nó báo quyền truy cập
`chmod 600 key_file`

![image](https://hackmd.io/_uploads/SJ3091ahGl.png)

Theo tìm hiểu thì do wsl ko hỗ trợ chỉnh sửa trực tiếp
Ta phải làm theo các bước :
>Tạo hoặc chỉnh sửa file `wsl.conf`:
>```=
>sudo nano /etc/wsl.conf
>```
>Thêm nội dung sau vào file (nếu chưa có):
>```=
>[automount]
>options = "metadata"
>```
>Lưu file (nhấn Ctrl+O, Enter, rồi Ctrl+X nếu dùng nano).
>Khởi động lại WSL bằng cách mở PowerShell hoặc Command Prompt của Windows (không phải terminal Linux) và gõ:
>```=
>wsl --shutdown
>```
>Mở lại terminal Linux (WSL). Bây giờ lệnh chmod 600 key_file trong thư mục /mnt/d/... của bạn sẽ hoạt động.

![image](https://hackmd.io/_uploads/S1Lxnyphfe.png)

![image](https://hackmd.io/_uploads/Hy1m31ahzl.png)

Flag là : `academy{k3y_5l3u7h_127b8b44}`