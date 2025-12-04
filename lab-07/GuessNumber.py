from random import randint
N=randint(0,99)
count=0


while True:
    s = input("输入一个整数(0-99): ")
    try:
        n = int(s)
    except ValueError:
        print("你输入了非整型数")
        continue

    count += 1
    if n > N:
        print("遗憾，太大了")
    elif n < N:
        print("遗憾，太小了")
    else:
        print(f"猜了{count}次，你猜中了!")
        break
    