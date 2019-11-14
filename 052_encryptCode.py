## 【问题】某个公司采用公用电话传递数据，数据是四位的整数，如2126 ，在传递过程中是加密的，
## 加密规则如下：每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。

def encrypt(ori_code):
    code_lst = []
    code_lst.append(ori_code % 10)
    code_lst.append(ori_code % 100 // 10)
    code_lst.append(ori_code % 1000 // 100)
    code_lst.append(ori_code // 1000)
    new_code = 0
    for i in range(4):
        code_lst[i] += 5
        code_lst[i] %= 10
        new_code = new_code + code_lst[i] * (10 ** (3 - i))
    return new_code
    
ori_code = int(input('请输入需要加密的四位整数：'))
outcome = encrypt(ori_code)
print(outcome)
