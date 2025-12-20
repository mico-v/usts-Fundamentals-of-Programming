from __future__ import annotations
import re
import sys
import csv
from pathlib import Path
from typing import List, Tuple

import requests
import matplotlib.pyplot as plt
import matplotlib

# 尝试使用系统中文字体以避免中文乱码/方块
matplotlib.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
matplotlib.rcParams["axes.unicode_minus"] = False

URL = "https://www.anjuke.com/fangjia/suzhou2022/"
DATA_CSV = Path(__file__).parent / "suzhou_2022_prices.csv"
OUTPUT_PNG = Path(__file__).parent / "suzhou_2022_prices.png"


def fetch_html(url: str) -> str:
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/121.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Referer": "https://www.anjuke.com/fangjia/",
    }
    resp = requests.get(url, headers=headers, timeout=20)
    resp.raise_for_status()
    return resp.text


def parse_month_price(html: str) -> List[Tuple[int, int]]:
    # 匹配形如： 2022年12月房价 ... 21089元/㎡ （中间可能有标签/空白）
    pattern = re.compile(r"2022年(\d{1,2})月房价[\s\S]{0,60}?([\d,]+)\s*元\s*/\s*㎡", re.S)
    pairs = []
    for m in pattern.finditer(html):
        month = int(m.group(1))
        price = int(m.group(2).replace(",", ""))
        pairs.append((month, price))
    # 去重并按月排序
    uniq = {}
    for month, price in pairs:
        uniq.setdefault(month, price)
    result = sorted(uniq.items(), key=lambda x: x[0])
    return result


def save_csv(month_price: List[Tuple[int, int]], csv_path: Path) -> None:
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["month", "price"])
        for m, p in month_price:
            writer.writerow([m, p])


def load_csv(csv_path: Path) -> List[Tuple[int, int]]:
    out: List[Tuple[int, int]] = []
    with csv_path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            out.append((int(row["month"]), int(row["price"])))
    return out


def plot_line(month_price: List[Tuple[int, int]], out_png: Path) -> None:
    months = [m for m, _ in month_price]
    prices = [p for _, p in month_price]

    plt.figure(figsize=(9, 4.8), dpi=120)
    plt.plot(months, prices, marker="o", linewidth=2, color="#1f77b4")
    plt.title("2022年苏州二手房均价 (安居客)")
    plt.xlabel("月份")
    plt.ylabel("均价 (元/㎡)")
    plt.xticks(range(1, 13))
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.savefig(out_png)


def main() -> int:
    # 优先尝试在线抓取；失败则回退到本地 CSV
    month_price: List[Tuple[int, int]] = []
    try:
        html = fetch_html(URL)
        month_price = parse_month_price(html)
        if month_price:
            save_csv(month_price, DATA_CSV)
            print(f"已抓取并保存到: {DATA_CSV}")
        else:
            print("未从页面解析到数据，尝试使用本地 CSV……")
    except Exception as e:
        print(f"抓取失败: {e}\n尝试使用本地 CSV……")

    if not month_price:
        if DATA_CSV.exists():
            month_price = load_csv(DATA_CSV)
            print(f"已从本地 CSV 读取: {DATA_CSV}")
        else:
            print("没有可用数据。")
            return 1

    plot_line(month_price, OUTPUT_PNG)
    print(f"折线图已输出: {OUTPUT_PNG}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
