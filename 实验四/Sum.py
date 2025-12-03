"""Sum.py
题目：先输入整型数 N（元素个数），再输入 N 个整型数（用逗号分隔），
分别用 while 和 for 两种循环计算序列之和并输出。

运行示例：
python Sum.py
请输入元素个数 N: 5
请输入 N 个整数（逗号分隔）: 1,2,3,4,5
while 求和结果: 15
for 求和结果: 15
"""

def parse_int_list(s: str):
    """把逗号分隔的字符串解析为整数列表；忽略空项；如果不能转换则抛出 ValueError。"""
    parts = [p.strip() for p in s.split(',') if p.strip() != '']
    return [int(x) for x in parts]


def sum_with_while(nums, limit):
    total = 0
    i = 0
    # 只累加最多 limit 个元素
    while i < len(nums) and i < limit:
        total += nums[i]
        i += 1
    return total


def sum_with_for(nums, limit):
    total = 0
    for x in nums[:limit]:
        total += x
    return total


def main():
    try:
        n = int(input("请输入元素个数 N: ").strip())
        if n <= 0:
            print("N 应为正整数，退出。")
            return
    except ValueError:
        print("输入的 N 不是合法整数，退出。")
        return

    s = input(f"请输入 N 个整数（逗号分隔），例如: 1,2,3,... : ").strip()
    try:
        nums = parse_int_list(s)
    except ValueError:
        print("解析整数列表失败，请确认所有项均为整数。")
        return

    if len(nums) < n:
        print(f"警告：你只输入了 {len(nums)} 个数，少于 N={n}，将按已输入个数计算。")

    s1 = sum_with_while(nums, n)
    s2 = sum_with_for(nums, n)

    print(f"while 求和结果: {s1}")
    print(f"for   求和结果: {s2}")


if __name__ == '__main__':
    main()
