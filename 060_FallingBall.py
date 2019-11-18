# 060_FallingBall.py
# 【问题】一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

class Ball:
    def __init__(self, height, distance = 0):
        self.height = height
        self.distance = 0
    
    def bounce(self, time):
        bounce_dis = 0
        for i in range(1,time+1):
            self.distance += self.height + bounce_dis
            self.height = self.height * 0.5
            bounce_dis = self.height
            
h = int(input('请输入初始高度（米）：'))
t = int(input('请输入反弹次数：'))
ball = Ball(h)
ball.bounce(t)
print('第%d次落地时，小球经过%f 米' % (t, ball.distance))
print('第%d次反弹，小球的高度是%f 米' % (t, ball.height))
