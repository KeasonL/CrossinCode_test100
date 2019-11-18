## 递归问题2
## 【问题】利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。

def reverse_str(ori_str, i):
    if i == 0:
        return
    print(ori_str[i-1])
    reverse_str(ori_str, i-1)

ori_str = input('请输入：')
i = len(ori_str)
reverse_str(ori_str, i)
