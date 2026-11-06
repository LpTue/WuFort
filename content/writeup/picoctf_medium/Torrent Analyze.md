---
title: Torrent Analyze
tags: ["PicoCTF_Medium"]
---

Tải bài tập tại [đây](https://learn.cylabacademy.org/library/311?page=1&category=4&difficulty=2&workspace=true&solved=true)

Đọc sơ qua về miêu tả ta thấy liên quan tới protocol BT-DHT

![image](https://hackmd.io/_uploads/B1bJdoT2fg.png)

Tìm hiểu sơ qua về BT-DHT ta biết được rằng nó sẽ mã hóa thành hash MD1 trước khi chia sẻ lên internet

![image](https://hackmd.io/_uploads/rkDHuo62zx.png)
Đầu tiên lần theo DNS ta thấy ip == 192.168.73.132 đang tải file từ torrent ubuntu

![image](https://hackmd.io/_uploads/SJG2ui63Mx.png)

Khi lọc với ip.src thì ta thấy nó đang lấy file liên tục từ các Leechers
Lướt lúc ta sẽ thấy protocol BT-DHT như bài đã đề cập

![image](https://hackmd.io/_uploads/HJYGYjT3Ml.png)

Lọc với protocol và ip.src ta sẽ thấy 2 mã hash khác nhau
`17d62de1495d4464f6fb385bdfd7ead5c897ea22`
`e2467cbf021192c241367b892230dc1e05c0580e`
Search hash tại web [này](https://archive.org/search?tab=all)

![image](https://hackmd.io/_uploads/B1EuKoT2Gl.png)

Ta thấy với hash này thì ta thu được là ubuntu

![image](https://hackmd.io/_uploads/BkmjKop3fe.png)

Flag là : `academy{ ubuntu-19.10-desktop-amd64.iso}`