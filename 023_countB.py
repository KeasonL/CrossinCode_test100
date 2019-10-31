## 【问题】从控制台输入一段字符，统计字符'b'出现次数
string = input('请输入一段字符')
b_sum = 0
for letter in string:
    if letter == 'b':
        b_sum += 1
print('共有%d 个字符“b”' % b_sum)
