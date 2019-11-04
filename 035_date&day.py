## 【问题】输入某年某月某日，判断这一天是这一年的第几天？
## 【分析】程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天

def isLeapYear(year):
    leap = False
    if year % 100 == 0:
        if year % 400 == 0:
            leap = True
    elif year % 4 == 0:
        leap = True
    return leap

while True:
    mth_day_list = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    print('输入q退出')
    yr = input('请输入年份:')
    mth = input('请输入月份:')
    dt = input('请输入日期:')
    if yr == 'q' or mth == 'q' or dt == 'q':
        break
    try:
        yr = int(yr)
        mth = int(mth)
        dt = int(dt)
        if isLeapYear(yr):
            mth_day_list[2] = 29
        day = 0
        for m in range(1, mth):
            day += mth_day_list[m]
        day += dt
        print('%d年%d月%d日是该年度的第%d天'%(yr, mth, dt, day))
    except:
        print('请按要求输入')
print('退出')
