## 根据输入年份判断二月的天数
## 【问题】实际为判断闰年

def isLeapYear(year):
    leap = False
    if year % 100 == 0:
        if year % 400 == 0:
            leap = True
    elif year % 4 == 0:
        leap = True
    return leap

yr = int(input('请输入年份:'))
if isLeapYear(yr):
    print('%d年2月有29日' % yr)
else:
    print('%d年2月有28日' % yr)
