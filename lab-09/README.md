https://www.anjuke.com/fangjia/suzhou2022/
分析这个网页的数据:2022年苏州的房价数据,月份和价格.并且把数据抓取下载保存,最后写一个python程序,把数据做成一个折线图

## 运行说明

- 安装依赖（根目录一次性安装）：

```bash
pip install -r requirements.txt
```

- 生成并查看折线图（包含抓取→保存CSV→绘图）：

```bash
python lab-09/suzhou_price_plot.py
```

- 产物：
	- 数据：lab-09/suzhou_2022_prices.csv（已内置一份，脚本也会更新）
	- 图片：lab-09/suzhou_2022_prices.png

若在线抓取失败，脚本会自动回退读取本地 CSV 再作图。