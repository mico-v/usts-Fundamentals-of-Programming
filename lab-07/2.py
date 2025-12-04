import csv
import os

def process_scores():
    # 定义学生成绩字典
    scores_dict = {"王小明": 87, "李华": 79, "张三": 92, "赵四": 66}
    csv_filename = "scores.csv"

    print(f"原始字典数据: {scores_dict}")

    # 1. 将字典保存为 CSV 文件
    # newline='' 是为了防止在 Windows 下产生空行
    try:
        with open(csv_filename, 'w', newline='', encoding='utf-8-sig') as f:
            # 使用 csv.writer
            writer = csv.writer(f)
            # 写入表头
            writer.writerow(["姓名", "成绩"])
            # 写入数据
            for name, score in scores_dict.items():
                writer.writerow([name, score])
        print(f"成功写入文件: {csv_filename}")
    except IOError as e:
        print(f"写入文件时出错: {e}")
        return

    print("-" * 20)

    # 2. 读取 CSV 文件并展示
    print("读取 CSV 文件内容:")
    try:
        with open(csv_filename, 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            # 读取所有行
            rows = list(reader)
            
            # 打印每一行
            for row in rows:
                print(row)
                
    except IOError as e:
        print(f"读取文件时出错: {e}")

if __name__ == "__main__":
    process_scores()