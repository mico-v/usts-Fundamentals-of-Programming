# 2、回文数判断。
# 回文数的定义：设n是一任意自然数。
# 若将n的各位数字反向排列所得自然数n1与n相等，则称n为一回文数。
# 例如，若n=1234321，则称n为一回文数；但若n=1234567，则n不是回文数。


n = input("请输入一个整数n:")
ans=True

for i in range(len(n)//2):
    if n[i]==n[-i-1]:
        pass
    else:
        ans=False

print("是回文数" if ans else "不是回文数")