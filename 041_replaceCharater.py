## 【问题】使用 * 替换字符串‘你好，我好，大家好才是真的好！’中的‘好’。

# 方法一
string = '你好，我好，大家好才是真的好！'
new_str = string.replace('好','*')
print(string)
print(new_str)

# 方法二
string = '你好，我好，大家好才是真的好！'
st_list = list(string)
for i in range(len(st_list)):
    if st_list[i] == '好':
        st_list[i] = '*'
new_str = ''.join(st_list)
print(string)
print(new_str)
