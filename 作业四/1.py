# 1． 羊车门问题（Monty Hall）- 蒙特卡罗模拟
# 有3扇门：1辆车、2只羊。参赛者先选1扇，主持人（知道答案）再打开另一扇有羊的门，
# 参赛者可以选择保持原选择或改为剩下那扇门。问：更换是否能提高中奖概率？

# import random
# import sys






from random import randint

countNochange=countChange=0
times=1000

for _ in range(times):
    car=randint(0,2)
    door=[False,False,False]
    door[car]=True
    choice=randint(0,2)
    for i in range(3):
        if not door[i] and i!=choice:
            if door[choice]:countNochange+=1
            else: countChange+=1
            break

print(f"更换门中奖的概率是{countChange/times:.2%}")
print(f"不更换门中奖的概率是{countNochange/times:.2%}")




