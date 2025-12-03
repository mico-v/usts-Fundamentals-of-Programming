import math

def isPrime(n):
    """
    判断一个整数是否为素数
    :param n: 待判断整数
    :return: True if prime, False otherwise
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
        
    # 只需要判断到 sqrt(n)
    limit = int(math.sqrt(n)) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True

def TwoPrimes(n):
    """
    将偶数 n 拆分成两个素数之和
    :param n: 大于2的偶数
    :return: (prime1, prime2)
    """
    # 遍历从 2 到 n/2
    for i in range(2, n // 2 + 1):
        if isPrime(i):
            j = n - i
            if isPrime(j):
                return i, j
    return None, None

if __name__ == "__main__":
    print("验证哥德巴赫猜想 (4 ~ 100):")
    count = 0
    for num in range(4, 101, 2):
        p1, p2 = TwoPrimes(num)
        if p1 is not None:
            # 格式化输出，例如 24=5+19
            print(f"{num}={p1}+{p2}", end='\t')
            count += 1
            # 每行打印 5 个
            if count % 5 == 0:
                print()
        else:
            print(f"{num} 无法拆分为两个素数之和 (反例?)", end='\t')
    print("\n验证完成。")
