import math

# 匿名函数计算判别式 delta = b^2 - 4ac
calc_delta = lambda a, b, c: b**2 - 4*a*c

def solve(a, b, c):
    """
    求解一元二次方程 ax^2 + bx + c = 0
    :param a: 二次项系数
    :param b: 一次项系数
    :param c: 常数项
    :return: (root1, root2) 或 (None, None)
    """
    delta = calc_delta(a, b, c)
    
    if delta < 0:
        return None, None
    elif delta == 0:
        x = -b / (2 * a)
        return x, x
    else:
        sqrt_delta = math.sqrt(delta)
        x1 = (-b + sqrt_delta) / (2 * a)
        x2 = (-b - sqrt_delta) / (2 * a)
        return x1, x2

if __name__ == "__main__":
    print("求解一元二次方程 ax^2 + bx + c = 0")
    try:
        user_input = input("请输入系数 a, b, c (用逗号分隔): ")
        # 处理可能包含空格的情况
        parts = user_input.replace('，', ',').split(',')
        if len(parts) != 3:
            raise ValueError("需要输入三个参数")
            
        a, b, c = map(float, parts)
        
        if a == 0:
            print("系数 a 不能为 0，这不是一元二次方程。")
        else:
            root1, root2 = solve(a, b, c)
            
            if root1 is None:
                print(f"方程 {a}x^2 + {b}x + {c} = 0 无实根")
            elif root1 == root2:
                print(f"方程 {a}x^2 + {b}x + {c} = 0 有两个相等的实根: x1 = x2 = {root1}")
            else:
                print(f"方程 {a}x^2 + {b}x + {c} = 0 有两个不相等的实根: x1 = {root1}, x2 = {root2}")
                
    except ValueError as e:
        print(f"输入错误: {e}。请确保输入三个数字并用逗号分隔。")
    except Exception as e:
        print(f"发生错误: {e}")
