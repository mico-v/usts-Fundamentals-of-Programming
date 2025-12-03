import math

a = int(input("请输入一个整数: "))
b = float(input("请输入一个实数: "))
c = int(b+0.5)


a3 = a * a * a
b3 = b * b * b


a2 = math.sqrt(a)
b2 = math.sqrt(b)

print(f"整数的三次方: {a3:.2f}, 开平方: {a2:.2f}")
print(f"实数的三次方: {b3:.2f}, 开平方: {b2:.2f}")