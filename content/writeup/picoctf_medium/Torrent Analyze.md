---
title: Torrent Analyze
tags: ["PicoCTF_Medium"]
---

Tải bài tập tại [đây](https://learn.cylabacademy.org/library/311?page=1&category=4&difficulty=2&workspace=true&solved=true)

Đọc sơ qua về miêu tả ta thấy liên quan tới protocol BT-DHT

![image](/images/617bef33e95598f4920f1c8fb34e324d.png)

Tìm hiểu sơ qua về BT-DHT ta biết được rằng nó sẽ mã hóa thành hash MD1 trước khi chia sẻ lên internet

![image](/images/baa116647d09222c601f50750e38bf07.png)
Đầu tiên lần theo DNS ta thấy ip == 192.168.73.132 đang tải file từ torrent ubuntu

![image](/images/ac64d8ee191313219c62d62c381771f4.png)

Khi lọc với ip.src thì ta thấy nó đang lấy file liên tục từ các Leechers
Lướt lúc ta sẽ thấy protocol BT-DHT như bài đã đề cập

![image](/images/d083a7dc2ae96d9c059ec5cdbc33833a.png)

Lọc với protocol và ip.src ta sẽ thấy 2 mã hash khác nhau
`17d62de1495d4464f6fb385bdfd7ead5c897ea22`
`e2467cbf021192c241367b892230dc1e05c0580e`
Search hash tại web [này](https://archive.org/search?tab=all)

![image](/images/31a9a47e26c60b24e5f590509031a923.png)

Ta thấy với hash này thì ta thu được là ubuntu

![image](/images/d9763e9345f12f212735063105331df8.png)

Flag là : `academy{ ubuntu-19.10-desktop-amd64.iso}`