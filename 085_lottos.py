# 双色球
# 【问题】根据福利彩票双色球玩法规则，6个蓝色球，范围为1 ~ 33，不允许重复，1个红色球，范围为1 ~ 16，自动生成6个蓝色球，1个红色球。

import random

def lottos():
    blue = list(random.sample(range(1,34), 6))
    red = random.randint(1,17)
    lottos_lst = [blue, red]
    return lottos_lst

lottos()
