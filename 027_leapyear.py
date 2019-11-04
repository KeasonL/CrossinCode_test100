## 【问题】判断闰年
## 【分析】百年除以400，非百年除以4，能除尽则为闰年
year = int(input('请输入年份：'))
leap = False
if year % 100 == 0:
    if year % 400 == 0:
        leap = True
elif year % 4 == 0:
    leap = True

if leap == True:
    print('%d 年是闰年' % year)
else:
    print('%d 年不是闰年' % year)
    
# 方法二
import calendar
for n in range(1950,2050):
    check_year=calendar.isleap(n)
    if check_year == True:
        print ("{}闰年".format(n))
