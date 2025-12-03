# 3．	猜数问题中的异常处理解决方法。
# 在程序中预设一个0~99之间的整数，让用户通过键盘输入所猜的数，如果大于预设的数，显示“遗憾，太大了”;
# 小于预设的数，显示“遗憾，太小了”，如此循环，直至猜中该数，显示“预测N次，你猜中了!”，
# 其中N是用户输入数字的次数。如果输入非整数，进行异常处理，显示“你输入了非整型数”


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
    