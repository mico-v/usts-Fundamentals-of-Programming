# 4. 随机生成包含1000个字符的字符串，然后统计每个字符的出现次数。
import random

# 生成1000个随机字符（小写字母）
random_chars = [chr(ord('a') + random.randint(0, 25)) for _ in range(1000)]
random_string = "".join(random_chars)

print(f"生成的字符串(前50个): {random_string[:50]}...")
# 输出: 生成的字符串(前50个): saagdplnhriutghvjgoynlsmyzesmefzszuepitevswrugbxdl...

# 统计次数
stats = {}
for char in random_string:
    stats[char] = stats.get(char, 0) + 1

print("字符统计结果:")
# 输出: 字符统计结果:
# 排序输出
for char in sorted(stats.keys()):
    print(f"'{char}': {stats[char]}次")
# 输出:
# 'a': 41次
# ...
# 'z': 34次
