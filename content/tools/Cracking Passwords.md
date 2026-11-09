---
title: Cracking Passwords
tags: ["Tools"]
---

# I. Mật khẩu và Mã băm
- Mật khẩu thường được lưu dưới dạng mã băm
- Khi nhập pass ngta sẽ so sánh mã băm để xác nhận đúng hay sai
- Nhiều hàm băm gồm `MD5`, `SHA-1`, `SHA-2`, `SHA-3`, `Bcrypt`, `Scrypt`, `Argon2`

# II. Bẻ khóa
- Có nhiều kiểu tấn công gồm brute-force, danh sách và kiểu rainbow table attack
- Trước hết cần xác định kiểu mã băm

### Cài công cụ xác định mã băm
```=
sudo apt install hash-identifier
```

![image](https://lptue.github.io/WuFort/images/17a12a5b4a825f2278a358294d2fb214.png)

Ví dụ với mã `098f6bcd4621d373cade4e832627b4f6` xác định là mã `MD5` hoặc `Domain Cached Credentials`


### Brute-force Attack
- Là kỹ thuật thử mọi tổ hợp có thể --> hơi mất thời gian
- Cài công cụ `sudo apt install hashcat`
- File hướng dẫn `hashcat` : tại [đây](https://github.com/LpTue/Forensics/blob/main/L%C6%B0u%20tr%E1%BB%AF/hashcat.html)

### Tấn công danh sách
- Là kỹ thuật thử mọi pass từ danh sách tới khi khớp
- Cài công cụ `sudo apt install john`
- File hướng dẫn John : tại [đây](https://github.com/LpTue/Forensics/blob/main/L%C6%B0u%20tr%E1%BB%AF/john.html)
- File hướng dẫn 2John : tại [đây](https://github.com/LpTue/Forensics/blob/main/L%C6%B0u%20tr%E1%BB%AF/2john.docx)
