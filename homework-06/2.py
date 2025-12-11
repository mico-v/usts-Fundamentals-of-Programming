import csv
import os

csv_path = os.path.join(os.path.dirname(__file__), 'mnist_test.csv')

with open(csv_path, 'r') as f:
    reader = csv.reader(f)
    next(reader) # skip header
    for i, row in enumerate(reader):
        if i >= 10: break
        print(f"Label: {row[0]}")
        pixels = row[1:]
        for r in range(28):
            line = "".join(["#" if int(p) > 0 else " " for p in pixels[r*28:(r+1)*28]])
            print(line)
