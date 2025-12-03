import math

s = input("请输入弧度值：").strip()
try:
    rad = float(s)
    deg = rad * 180 / math.pi
    print(f"{rad:g} 弧度 = {deg:.6f} 度")
except ValueError:
    print("输入格式错误")