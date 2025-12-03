# 2．	最大公约数与最小公倍数计算问题。
# 输入两个整型数，计算出它们的最大公约数和最小公倍数，并输出结果。
import math
a, b = map(int, input("请输入两个整数").split())
g = math.gcd(a,b)
l = math.lcm(a,b)
print(f"最大公约数是{g},最小公倍数是{l}")