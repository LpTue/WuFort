---
title: Weird File
tags: ["PicoCTF_Medium"]
---

Tải bài tập tại [đây](https://learn.cylabacademy.org/library/101?page=4&category=4&difficulty=2&workspace=true)
Đọc kỹ giới thiệu

![image](https://hackmd.io/_uploads/HyVlR3U5Ml.png)

Ta nghĩ ngay tới bị giấu macro

![image](https://hackmd.io/_uploads/ry-QChIcGg.png)

Ta dùng tool lấy chuỗi ra
```doc=
Sub AutoOpen()
    MsgBox "Macros can run any program", 0, "Title"
    Signature

End Sub

 Sub Signature()
    Selection.TypeText Text:="some text"
    Selection.TypeParagraph

 End Sub

 Sub runpython()

Dim Ret_Val
Args = """" '"""
Ret_Val = Shell("python -c 'print(\"cGljb0NURnttNGNyMHNfcl9kNG5nM3IwdXN9\")'" & " " & Args, vbNormalFocus)
If Ret_Val = 0 Then
   MsgBox "Couldn't run python script!", vbOKOnly
End If
End Sub
```
Thấy đoạn đáng ngờ 
`cGljb0NURnttNGNyMHNfcl9kNG5nM3IwdXN9`

![image](https://hackmd.io/_uploads/r11DA3I9zx.png)

Ta đưa về dạng academy

![image](https://hackmd.io/_uploads/S10D02I5Gg.png)

Flag là : academy{m4cr0s_r_d4ng3r0us}