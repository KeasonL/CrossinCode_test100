## 【问题】输入一行字符，如'are you ok ! 黎明。'。分别统计出其中英文字母、空格、数字和其它字符的个数。

string = input('请输入一段文字')
letters = 0
spaces = 0
digits = 0
others = 0
i=0
while i < len(string):
    charater = string[i]
    i += 1
    if charater.isalpha():
        letters += 1
    elif charater.isspace():
        spaces += 1
    elif charater.isdigit():
        digits += 1
    else:
        others += 1
print('共有字符 %d个' % len(string))
print('英文字符 = %d, 空格 = %d, 数字 = %d, 其他字符 = %d' % (letters, spaces, digits, others))
