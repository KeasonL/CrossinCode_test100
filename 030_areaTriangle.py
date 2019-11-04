## 【问题】输入三角形三个边求计算三角形的面积
## 【分析】"三角形两边之和大于第三边，S=sqrt[p(p-a)(p-b)(p-c)]"
from math import sqrt
a = float(input('请输入三角形的第1条边'))
b = float(input('请输入三角形的第2条边'))
c = float(input('请输入三角形的第3条边'))
d = [a, b, c]
d.sort()
if (d[0] + d[1]) > d[2]:
    p = (a + b + c)/2
    area_t = sqrt(p * (p - a) * (p - b) * (p - c))
    print('三角形的面积是%.2f' % area_t)
else:
    print('未能构成三角形')
