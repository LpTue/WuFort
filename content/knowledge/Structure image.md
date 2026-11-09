---
title: Structure image
tags: ["Knowledge"]

---

# I. Tìm hiểu về thành phần tạo nên một ảnh
## Tìm hiểu về kích thước của một ảnh
- Mỗi bức ảnh đều được tạo nên từ rất nhiều Pixel

![image](/images/8ff85a8eecc0f462bd02a1257cef6c6a.png)

- Nếu số lượng Pixel càng lớn thì size ảnh càng to 
- Size ảnh to làm tăng độ phân giải, tăng độ chi tiết của ảnh

## Tìm hiểu về Bit Depth ( True color )
- Có thể hiểu đơn giải để tạo nên một pixel, thì cần bit depth
- Bit depth quyết định số lượng màu sắc của một ảnh
    > 1 bit = 2 màu
    > 2 bit = $2^2$ = 4 màu
    > 3 bit = $2^3$ = 8 màu
    > 4 bit = $2^4$ = 16 màu
    > 6 bit = $2^6$ = 64 màu
    > 8 bit = $2^8$ = 256 màu
    > 16 bit = $2^{16}$ = 65536 màu
    > 32 bit = $2^{32}$ = 4294967296 màu 
- Bit depth càng cao thì ảnh cho ra có chất lượng màu càng nét
- True color là màu RGB cơ bản ( Red, Green, Blue )
- True color + Alpha ( thêm độ trong suốt ), Alpha có kênh từ ( 0 - 256 ) tương ứng với 256 kênh
- Với 24 bit True color + Alpha = $(25 \times \frac{24}{8}^3)$ màu

![image](/images/8c14d195f739f73f2dfd4ec163dab22c.png)

# II. Tìm hiểu về cách định dạng ảnh
## Lý do có các định dạng ảnh
- Lấy ví dụ với ảnh 640x480 pixel và 24 bit màu
    > Có 640x480x24 = 7372800 bits = 921600 bytes = 900KB
- Có thể thấy khi độ phân giải càng cao và số lượng bit màu càng lớn thì dung lượng ảnh càng lớn
- Vì vậy có các thuật toán nén ảnh khác nhau ( các định dạng ảnh )
## Thuật toán nén không mất dữ liệu
- Là thuật toán làm giảm dung lượng nhưng không làm giảm chất lượng
- Đại diện cho thuật toán này gồm có ảnh PNG
    > Tạm hiểu khi có một dải màu giống nhau thì PNG tìm cách ghi ngắn hơn thay vì ghi tám màu cùng một lượt
    > Điều đó khiến dữ liệu không bị mấ
    > ![image](/images/592af7b410184bb25a3f24929e30d6de.png)

## Thuật toán nén ảnh mất dữ liệu
- Là thuật toán lưu ảnh trông có vẻ hoàn hảo nhưng không vì đã bị cắt xén dữ liệu
- Đại diện cho thuật toán này gồm các ảnh JPG ( hay JPEG )
    > Mắt người thường nhạy các độ sáng + đường nét, và ít hơn với chi tiết màu
    > Vì vậy chúng chia ảnh thành các khối nhỏ, những biến đổi khó thấy bị làm tròn hoặc bỏ đi
    > ![image](/images/65f874e994ccb5ae2815b5aacfbd96d7.png)

# III. Đi sâu vào cấu trúc file png
- Chi tiết tại [đây](https://en.wikipedia.org/wiki/PNG#)
- Ngắn gọn thì file png gồm có 4 phần quan trọng gồm `IHDR`,`PLTE`,`IDAT`,`IEND`
> `IHDR` có thể phát hiện bằng pngcheck
> `PLTE` bắt buộc có khi 
>![image](/images/f28b72d9940d7b8b9c5004af3d8d00ce.png)
> `IDAT` chứa hình ảnh, có thể chia thành nhiều phần IDAT
> `IEND` đánh dấu kết thúc ảnh
- Và các phần phụ trợ
