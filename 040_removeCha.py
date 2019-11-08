## 【问题】Python 移除字符串中的指定位置字符,"Crossin 的编程教室"  中第八位空白符

string = input('请输入任意内容：')
locate = int(input('请输入你想要移除字符串的位置：'))

st_list = list(string)
st_list.pop(locate-1)

print('原字符是:%s,被删除的位置是：%s'%(string, locate))
print('删除后指定位置后的字符串为：%s'%''.join(st_list))
