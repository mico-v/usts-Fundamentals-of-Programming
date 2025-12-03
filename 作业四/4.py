# 4．	穷举算法：百鸡问题。
# 公鸡每只5元，母鸡每只3元，小鸡3只1元。用100元钱买100只鸡，求公鸡、母鸡、小鸡只数。


for roosters in range(21):   
    for hens in range(34):   
        chicks = 100 - roosters - hens
        if chicks < 0:
            continue
        if 15 * roosters + 9 * hens + chicks == 300:
            print(f"公鸡: {roosters} 只, 母鸡: {hens} 只, 小鸡: {chicks} 只")



