# 2．用求质数问题，解哥德巴赫猜想问题。
# 所谓哥德巴赫猜想是指：任意大于2的偶数都可以写成两个质数之和。
# 例如：6 = 3+3, 8=3+5，…，18=7+11。

from sympy import primerange

num=int(input("输入测试范围:"))
primes = set(primerange(2, num))
ans=True
for n in range(4, num+1, 2):
    found=False
    for p in primes:
        q = n - p # pyright: ignore[reportOperatorIssue]
        if q in primes:
            print(f"{n} = {p} + {q}")
            found=True
            break
    if not found:
        ans=False

print(f"在2到{num}范围内,哥德巴赫猜想{"正确"if ans else "不正确"}")