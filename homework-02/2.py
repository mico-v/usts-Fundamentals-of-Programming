# 猴子吃桃：第10天早上剩 1 个，倒推求第一天数量
days = 10
peaches = 1  # 第10天早上剩余
for _ in range(days - 1):
    peaches = 2 * (peaches + 1)  # 前一天早上的数量
print(peaches)  # 输出：1534


print((lambda d: __import__('functools').reduce(lambda p, _: 2*(p+1), range(d-1), 1))(10))