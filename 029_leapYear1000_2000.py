## 【问题】输出1000-2000之间的闰年

import calendar
for n in range(1000,2001):
    check_year=calendar.isleap(n)
    if check_year == True:
        print ("{}是闰年".format(n))
print('END')
