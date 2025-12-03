rate = 7.15  # 1 美元 = 7.15 人民币

s = input("请输入金额（人民币以R结尾，美元以U结尾）").strip()
if not s:
    print("输入为空")
else:
    unit = s[-1].upper()
    num_str = s[:-1].strip()
    try:
        amount = float(num_str)
    except ValueError:
        print("金额格式错误")
    else:
        match unit:  # 需要 Python 3.10+
            case 'R':
                usd = amount / rate
                print(f"{amount:.2f}R = {usd:.2f}U")
            case 'U':
                rmb = amount * rate
                print(f"{amount:.2f}U = {rmb:.2f}R")
            case _:
                print("尾字母应为 R 或 U")