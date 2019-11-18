## 回文数判断
## 【问题】一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。

n = int(input('请输入一个5位数：'))
def isPalindrome(n):
    n1 = n % 10
    n2 = n % 100 // 10
    n3 = n % 1000 // 100
    n4 = n % 10000 // 1000
    n5 = n // 10000
    if n1 == n5 and n2 == n4:
        return True
    else:
        return False

if isPalindrome(n):
    print('%d是回文数' % n)
else:
    print('%d不是回文数' % n)
