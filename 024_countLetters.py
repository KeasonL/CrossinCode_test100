## 【问题】从控制台输入一段字符，统计字符出现次数
string = input('请输入一段文字')
letters = {}
for charater in string:
    if charater in letters:
        letters[charater] += 1
    else:
        letters[charater] = 1
for charater in letters:
    print('%s 字符在这段文字中出现了%d 次' %(charater, letters[charater]))
