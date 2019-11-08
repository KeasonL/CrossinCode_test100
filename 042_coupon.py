## 【问题】生成优秀券号码很多付费应用的开发者，会设计一些优惠券来吸引用户来使用新开发的应用，以达到一定的广告效应。
## 现在，请你帮他们设计并生成200个优惠券号码。优惠码的字符由26个英文字符（大小写）组成，每个优惠码有8位

import random, string
letters = string.ascii_letters
coupon = []
while len(coupon) < 200:
    str_coupon = ''
    for i in range(8):
        str_coupon += random.choice(letters)
    if str_coupon not in coupon:
        coupon.append(str_coupon)
for j in range(0,200,10):
    print(coupon[j:j+10])
