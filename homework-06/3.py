import csv
import random
import os

base = os.path.dirname(__file__)
with open(os.path.join(base, 'dictionary.csv'), 'r', encoding='gb2312') as f:
    lines = list(csv.reader(f))

selected = random.sample(lines, 50)

with open(os.path.join(base, 'study.txt'), 'w', encoding='utf-8') as f:
    for row in selected:
        f.write(f"{row[0]} {row[1]}\n")
