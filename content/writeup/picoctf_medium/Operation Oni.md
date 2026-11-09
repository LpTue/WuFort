---
title: Operation Oni
tags: ["PicoCTF_Medium"]
---

Tải bài tập tại [đây](https://learn.cylabacademy.org/library/284?page=1&category=4&difficulty=2&workspace=true&solved=true)

Ta tìm thấy file mã

![image](/images/dbc48047105dfc6697534e833adcdc02.png)

Ta trích xuất file dưới dạng `key_file`

![image](/images/7b5e423d3d2e6a581601cf84a00afce4.png)

![image](/images/e88ab7bf1d8778fccfe8cdd8af291f46.png)

Theo log thì nó báo quyền truy cập
`chmod 600 key_file`

![image](/images/0bfdab36bb75717619cf1e8de4ff7fb7.png)

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

![image](/images/e8b7031027f9b96b4cdba295e03a4f01.png)

![image](/images/14a02958302b96327a53796ba65f158e.png)

Flag là : `academy{k3y_5l3u7h_127b8b44}`