import pandas as pd
import matplotlib.pyplot as plt

# 设置中文字体，防止乱码
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取数据
df = pd.read_csv('stock.csv')

# 计算每日涨幅：(收盘-开盘)/开盘
df['涨幅'] = (df['收盘'] - df['开盘']) / df['开盘']

# 1. 绘制收盘指数变化折线图
plt.figure(figsize=(10, 5))
plt.plot(df['日期'], df['收盘'], marker='o')
plt.title('上证指数收盘价变化')
plt.xlabel('日期')
plt.ylabel('收盘指数')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. 绘制每日指数涨幅直方图 (柱状图)
plt.figure(figsize=(10, 5))
plt.bar(df['日期'], df['涨幅'])
plt.title('每日指数涨幅')
plt.xlabel('日期')
plt.ylabel('涨幅')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
