## 【问题】给定一个字符串如 "Crossin的编程教室"，然后将其翻转，逆序输出。

string = 'Crossin的编程教室'
# 方法一
new_string = ''.join(reversed(string))
print(new_string)

#方法二
print(string[::-1])
