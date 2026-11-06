---
title: CTQ1
tags: ["MiniCTF"]

---

Khi đọc file pcap ta thấy ó file script.ps1

![image](https://hackmd.io/_uploads/HksUWXg9fe.png)

Export HTTP object list ta được `flag.txt` và `script.ps1`
Ta mở file `flag.txt` thấy flag giả

![image](https://hackmd.io/_uploads/SJhs-Qe9Gg.png)

![image](https://hackmd.io/_uploads/HyY3b7l9Me.png)

Đọc code của file `.ps1` tạm hiểu

- Đầu tiên file được mã hóa base64 2 lần
- Sau đó đổi "=" thành "-"
- Sau đó upload lên thông qua FTP

Ta export toàn bộ FTP-DATA object list

![image](https://hackmd.io/_uploads/SJZufQe9Ml.png)

Sau đó ta viết chương trình dịch ngược đoạn mã hóa

```python=
import base64
import os
import sys


def giai_ma_ten_file(ten_file):
    # 1. Lược bỏ "upload%2f"
    ten_file = ten_file.removeprefix("upload%2f")

    # 2. Chuyển \_ thành =
    ten_file = ten_file.replace(r"\_", "=")

    # Nếu dữ liệu thực tế dùng "__" thay cho "\_\_"
    # thì xử lý luôn
    while ten_file.endswith("_"):
        ten_file = ten_file[:-1] + "="

    # 3. Base64 lần 1
    du_lieu = base64.b64decode(ten_file)

    # 4. Base64 lần 2
    du_lieu = base64.b64decode(du_lieu)

    # 5. Bytes -> UTF-8
    return du_lieu.decode("utf-8")


def doi_ten_trong_folder(folder):
    if not os.path.isdir(folder):
        print(f"[!] Không tìm thấy folder: {folder}")
        return

    so_luong = 0
    thanh_cong = 0
    that_bai = 0

    for ten_file in os.listdir(folder):
        duong_dan_cu = os.path.join(folder, ten_file)

        # Bỏ qua thư mục
        if not os.path.isfile(duong_dan_cu):
            continue

        so_luong += 1

        try:
            # Giải mã tên file
            ten_moi = giai_ma_ten_file(ten_file)

            duong_dan_moi = os.path.join(folder, ten_moi)

            # Kiểm tra tên mới đã tồn tại chưa
            if os.path.exists(duong_dan_moi):
                print(f"[!] Bỏ qua vì tên đã tồn tại:")
                print(f"    {ten_file}")
                print(f" -> {ten_moi}")
                that_bai += 1
                continue

            # Đổi tên
            os.rename(duong_dan_cu, duong_dan_moi)

            print("[+] Đổi tên thành công:")
            print(f"    {ten_file}")
            print(f" -> {ten_moi}")

            thanh_cong += 1

        except Exception as e:
            print(f"[X] Không giải mã được:")
            print(f"    {ten_file}")
            print(f"    Lỗi: {e}")
            that_bai += 1

    print("\n========== KẾT QUẢ ==========")
    print(f"Tổng file : {so_luong}")
    print(f"Thành công: {thanh_cong}")
    print(f"Thất bại  : {that_bai}")


if __name__ == "__main__":
    # Có thể truyền folder bằng command line
    if len(sys.argv) > 1:
        folder = sys.argv[1]
    else:
        folder = input("Nhập đường dẫn folder: ").strip()

    doi_ten_trong_folder(folder)
```

Đọc lại giới thiệu 

![image](https://hackmd.io/_uploads/S1KBLQecGg.png)

Nếu là học sinh thì thứ quan trọng sẽ nhắm tới đó là file đề thi

![image](https://hackmd.io/_uploads/ryoPUXl5fg.png)

Ta đem đi giải và được flag : KCSC{u_f0und_m3_n1c3_try}