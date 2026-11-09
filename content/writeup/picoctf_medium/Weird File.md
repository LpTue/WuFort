---
title: Weird File
tags: ["PicoCTF_Medium"]
---

Tải bài tập tại [đây](https://learn.cylabacademy.org/library/101?page=4&category=4&difficulty=2&workspace=true)
Đọc kỹ giới thiệu

![image](/images/b2badff56b97ecb2732254825a317f28.png)

Ta nghĩ ngay tới bị giấu macro

![image](/images/6d3b4b491a7541917163a2f9256b2d65.png)

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

![image](/images/a77da81f2e6947b7e219ecd4b19461c0.png)

Ta đưa về dạng academy

![image](/images/eb445753d9c562866f9661d39b768bc1.png)

Flag là : academy{m4cr0s_r_d4ng3r0us}