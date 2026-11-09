---
title: Oletools
tags: ["Tools"]
---

# I. Giới thiệu về Oletools
- Là gói công cụ phân tích các tệp Microsoft 
- Nó cung cấp công cụ để phân tích các tệp RTF và các tệp dựa trên định dạng OpenXML
- Cụ thể về Oletools cũng như các công cụ bao gồm tại [đây](https://www.decalage.info/hugo/python/oletools/)

# II. Kiểm tra file
- Tải file học tại [đây](https://github.com/vonderchild/digital-forensics-lab/blob/main/Lab%2003/files/YearlyBonus.docm)
- Là công cục hính để phát hiện tài liệu chứa bất kỳ macro này được nhúng bên trong hay không
- Sử dụng lệnh  `oleid <file>`

![image](https://lptue.github.io/WuFort/images/891cb9594c960cd68e1d37065d8df869.png)

- Có thể thấy mức độ rủi ro cao
- Giờ hãy sử dụng `olevba` để trích xuất macro
- Sử dụng lệnh `olevba <file>`

![image](https://lptue.github.io/WuFort/images/3371a176386a03cbcfb54b4b943c7ead.png)

Từ đó ta lấy được macro

# III. Mở rộng
- `olevba` : Đọc source code
- `dcodedmp` : Đọc P-Code ( Mã mà khi mở thì file sẽ ưu tiên chạy )

![image](https://lptue.github.io/WuFort/images/68897fba10c2e65086d462e254545ab5.png)


