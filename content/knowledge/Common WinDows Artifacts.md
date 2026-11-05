---
title: Common WinDows Artifacts
tags: ["Knowledge"]
---

# I. Giới thiệu
- Gồm tệp tin, thư mục, nhật ký, registry, lịch sử trình duyệt, tài khoản người dùng và các dữ liệu quan trọng khác

# II. Windows Registry 
- Là cơ sở dữ liệu phân cấp lưu trữ cấu hình người dùng, ứng dụng và thiết bị phần cứng
    > Chứa thông tin mà Win liên tục tham chiếu trong quá trình hoạt động
- Win Reg gồm năm nhanh chính, nằm dưới gốc Computer gồm
    >- `HKEY_CURRENT_USER (HKCU)` : Thông tin về người dùng đăng nhập, bao gồm màu sắc màn hình và control panel 
    >- `HKEY_USERS (HKU)` : Hồ sơ người dùng đang hoạt động trên hệ thống, bao gồm hồ sơ và cài đặt
    >- `HKEY_LOCAL_MACHINE (HKLM)` : Thông tin về cấu hình hệ thống ( cho bất kỳ người dùng nào )
    >- `HKEY_CLASSSES_ROOT (HKCR)` : Thông tin về các loại tệp và các chương trình liên kết với chúng
    >- `HKEY_CURRENT_CONFIG (HKCC)` : Thông tin về cấu hình phần cứng hệ thống

![image](https://hackmd.io/_uploads/Sk56vsn_Mg.png)

# III. NTUSER.DAT
- Là nhánh hồ sơ người dùng, một phần của registry. Cấu hình mỗi người được lưu trong `C:\Users\%USERNAME%\NTUSER.DAT`

![image](https://hackmd.io/_uploads/SJR_hMOFMl.png)

# IV. Tệp LNK
- Là tệp phím tắt cho phép truy cập vào các tệp, thư mục hoặc chương trình thường xuyên sử dụng hệ thống
- Có đuôi `.lnk` và thường tìm thấy ở màn hình desktop

![image](https://hackmd.io/_uploads/ryU50f_YGg.png)

- Dùng công cụ `LECmd` để phân tích thông tin hữu ích từ một tệp `.lnk`

![image](https://hackmd.io/_uploads/HJTzW7_Fzl.png)

# V. Trình duyệt Web
- Trình duyệt web cung cấp nhiều thông tin về lịch sử duyệt web, cookie, tệp tải về, mật khẩu lưu, v.v
- Chúng ta có thể tìm được 
>`C:\Users\%USERNAME%\AppData\Roaming\Mozilla\Firefox\Profiles` `.sqlite` `.json`
>`C:\Users\%USERNAME%\AppData\Local\Google\Chrome\User Data\Local State`
> Tùy từng trình duyệt sẽ lưu ở những vị trí khác nhau
- Có thể đọc bằng `DB Browser for SQLite`

![image](https://hackmd.io/_uploads/ry4sInqFze.png)

## Đăng nhập đã lưu
- Trình duyệt mã hóa các đăng nhập đã lưu bằng tệp nằm trong thư mục hồ sơ
- Để trích xuất sử dụng công cụ [này](https://github.com/unode/firefox_decrypt)

# VI. Nhật ký sự kiện
- Cung cấp hồ sơ về các sự kiện quan trọng của hệ thống, bảo mật và ứng dụng
- Sử dụng Event Viewer, công cụ tích hợp sẵn trên Win `C:\Windows\System32\winevt\Logs`
- Các loại nhật ký liên quan tới bảo mật gồm ( Không phải duy nhất )

![image](https://hackmd.io/_uploads/BkjEK29Yfg.png)

- Mỗi sự kiện đều có id cụ thể, có thể dùng để nhận diện và lọc các sự kiện cụ thể liên quan

![image](https://hackmd.io/_uploads/r1hTs3cKGl.png)


