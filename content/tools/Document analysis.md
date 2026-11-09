---
title: Document analysis
tags: ["Tools"]
---

# I. Tài liệu Microsoft 
- Những tài liệu có thể chứa các thông điệp ẩn hoặc mã độc hại có thể được thực thi khi ta mở các tài liệu này

## Tài liệu
- Có hai định dạng tệp được sử dụng chính gồm :
    > OLE ( Object Linking and Embedding : Liên kết và nhúng đối tượng )
    > OOOXML ( Office Open XML )
## OLE 
- Là định dạng cũ từ 1997 - 2003
- Định nghĩa cấu trúc " tệp trong tệp ", cho phép nhúng một tệp khác vào một tệp
    > Ví dụ : bảng tính Excel có thể nhúng vào tài liệu
- Hỗ trợ các tệp mở rộng tệp như `.rtf`, `.doc`, `ppt`, `xls`, cùng nhiều phần mở rộng khác

## OOXML
- Là định dạng tệp hiện đại dựa trên XML cho các tài liệu văn phòng
    > Tệp XML ( Extensible Markup Language : ngôn ngữ đánh đấu mở rộng ) là các file văn bản thuần túy mô tả cấu trúc và các tính năng khác của tài liệu 
- Các phần mở rộng tài liệu gồm `.docx`, `.pptx`, `xlsx`, cùng nhiều phần mở rộng khác
- Định dạng lưu các tài liệu dưới dạng các tệp Zip
- Bằng cách đổi tên phần mở rộng `.docx.zip`, `.xlsx.zip`, `pptx.zip`, bạn có thể giải nén nội dung các tệp thành các XML 
riêng lẻ

![image](https://lptue.github.io/WuFort/images/426641c39c436fb5bd2161429774b85b.png)

- Đây là tính năng hữu ích cho điều tra số, vì cho phép các nhà kiểm tra nội dung tài liệu mà không cần sửa đổi nó

## Cấu trúc giải nén của tài liệu OOXML
- Sau khi giải nén bằng cách thêm đuôi `.zip`

![image](https://lptue.github.io/WuFort/images/abb98a548b1eb5ea7ffedf2ce86d6339.png)

### [Content_Types].xml
- Là tệp chứa thông tin về các loại nội dung có trong tài liệu và phần mở rộng tệp tương ứng của chúng

### 📂 docProps
- Chứa `app.xml` và `core.xml`
- `app.xml` : chứa thông tin về ứng dụng sử dụng để tạo tài liệu
```xml=
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">
  <Template>Normal.dotm</Template>
  <TotalTime>0</TotalTime>
  <Pages>1</Pages>
  <Words>1</Words>
  <Characters>12</Characters>
  <Application>Microsoft Office Word</Application>
  <DocSecurity>0</DocSecurity>
  <Lines>1</Lines>
  <Paragraphs>1</Paragraphs>
  <ScaleCrop>false</ScaleCrop>
  <Company/>
  <LinksUpToDate>false</LinksUpToDate>
  <CharactersWithSpaces>12</CharactersWithSpaces>
  <SharedDoc>false</SharedDoc>
  <HyperlinksChanged>false</HyperlinksChanged>
  <AppVersion>16.0000</AppVersion>
</Properties>
```
-`core.xml` : chứa siêu dữ liệu của tài liệu, chẳng hạn như tên tác giả, ngày tạo và ngày sửa đổi
```xml=
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dc:title/>
  <dc:subject/>
  <dc:creator>Saad Javed</dc:creator>
  <cp:keywords/>
  <dc:description/>
  <cp:lastModifiedBy>Saad Javed</cp:lastModifiedBy>
  <cp:revision>2</cp:revision>
  <dcterms:created xsi:type="dcterms:W3CDTF">2023-02-04T15:44:00Z</dcterms:created>
  <dcterms:modified xsi:type="dcterms:W3CDTF">2023-02-04T15:44:00Z</dcterms:modified>
</cp:coreProperties>
```

### 📂 _rels
-`.rels` : chứa thông tin về mối quan hệ giữa các phần khác nhau của tài liệu, ví dụ như 'app.xml' và 'core.xml'

### 📂 word
- Thư mục này chứa nội dung thực tế của tài liệu
- `document.xml` : chứa nội dung văn bản thực tế của tài liệu
```xml=
 <w:body>
    <w:p w14:paraId="68F74602" w14:textId="442B891B" w:rsidR="00D473D4" w:rsidRPr="00B20485" w:rsidRDefault="00B20485">
      <w:pPr>
        <w:rPr>
          <w:lang w:val="en-US"/>
        </w:rPr>
      </w:pPr>
      <w:r>
        <w:rPr>
          <w:lang w:val="en-US"/>
        </w:rPr>
        <w:t>Hello World!</w:t>
      </w:r>
    </w:p>
    <w:sectPr w:rsidR="00D473D4" w:rsidRPr="00B20485">
      <w:pgSz w:w="11906" w:h="16838"/>
      <w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440" w:header="708" w:footer="708" w:gutter="0"/>
      <w:cols w:space="708"/>
      <w:docGrid w:linePitch="360"/>
    </w:sectPr>
  </w:body>
</w:document>
```
-`fontTable.xml` : chứa thông tin về các phông chữ được sử dụng trong tài liệu
- 📂 _rels : chứa tệp tin `document.xml.rels`
    > `document.xml.rels` : chứa thông tin về các mối quan hệ giữa các phần khác nhau của tài liệu, chẳng hạn như kiểu dáng, chủ đề, cài đặt cx như các URL cho liên kết bên ngoài
- `settings.xml` : chứa các cài đặt tài liệu và thông tin cấu hình
- `styles.xml` : chứa các thông tin về các kiểu định dạng được sử dụng trong tài liệu
- 📂 theme : chứa các tệp về chủ đề được sử dụng trong tài liệu
    > `theme1.xml` : chứa nội dung chủ đề thực tế
- `webSettings.xml` : chứa các thông tin về các cài đặt dành riêng cho web tài liệu, chẳng hạn như khung HTML cx như các định dạng lưu dưới dạng HTML

# II. Tài liệu hỗ trợ macro
- Là tập hợp các lệnh tự động hóa các tác vụ
- Macro được viết bằng Visual Basic for Applications ( VBA )
- Kẻ tấn công thường lợi dụng trong các cuộc tấn công lừa đảo và nhúng các mã độc để thực hiện hành động xấu và cài đặt phần mền vào hệ thống

![image](https://lptue.github.io/WuFort/images/f697866ca47191e0c5ca06ae5f5ae36d.png)

![image](https://lptue.github.io/WuFort/images/2c7781f64730e83ca2e7f671b76e65ed.png)

## Phân tích macro
- Đọc tại [đây](https://hackmd.io/@LpTue/SkRcH19uze)