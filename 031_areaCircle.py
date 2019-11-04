## 【问题】输入圆的半径求计算圆的面积，pi = 3.142
## 【分析】圆的面积公式: pi*r*r
r = float(input('请输入圆的半径'))
pi = 3.142
area_c = pi * (r ** 2)
print('圆的面积是%.2f' % area_c)
