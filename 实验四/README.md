三、实验内容  
	要求：对下列问题进行IPO分析，并画出流程图。
1、分别使用while、for构造循环程序，用于计算数列的和。
编写一个Python程序Sum.py。首先通过键盘输入一个整型数，表示数列的元素个数N，然后通过键盘连续输入N个整型数，每个整型数之间用逗号分隔。要求分别用while和for循环语句计算数列所有元素相加的和，并输出得到的和。
2、猜数字游戏。
编写一个Python程序GuessNumber.py。在程序中预设一个0~99之间的整数，让用户通过键盘输入所猜的数，如果大于预设的数，显示“遗憾，太大了”；如果小于预设的数，显示“遗憾，太小了”，如此循环，直至猜中该数，显示“预测N 次，你猜中了!”，其中N是用户输入猜测数字的次数。
四、实验步骤【图文方式叙述】

1、IPO分析与流程图

- 任务1 Sum.py（数列求和）
	- 输入(Input)：整型数 N（元素个数），以及以逗号分隔的 N 个整型数值字符串。
	- 处理(Process)：
		1. 解析输入的逗号分隔字符串为整数列表（忽略空项，若转换失败则提示错误并退出）。
		2. 用 while 循环对前 N 个元素求和（若实际输入少于 N，则按实际个数计算）。
		3. 用 for 循环对前 N 个元素求和（同上）。
	- 输出(Output)：两种方法计算的和（while 求和结果、for 求和结果）。

	流程图（已生成）：
	- 文件：`Sum_flowchart.png`
	- 生成脚本：`Sum_flowchart.py`（若需重新生成，运行 `python Sum_flowchart.py`，需安装 graphviz）

- 任务2 GuessNumber.py（猜数字游戏，已由学生完成）
	- 输入(Input)：用户交互式输入猜测整数（0-99）。
	- 处理(Process)：生成随机数 N；循环读取用户输入并尝试转换为整数；若非整型提示并重试；计次并比较大小，给出提示直到猜中。
	- 输出(Output)：提示“太大/太小”或“猜中了并输出尝试次数”。

	流程图（已生成）：
	- 文件：`GuessNumber_flowchart.png`
	- 生成脚本：`GuessNumber_flowchart.py`

2、源程序与运行记录

- `Sum.py`（文件路径：实验四/Sum.py）
	- 运行方式：
		1. 进入 `实验四` 目录：
			 ```powershell
			 cd 'd:\project\python\school\计算机程序设计基础\实验四'
			 ```
		2. 运行：
			 ```powershell
			 python Sum.py
			 ```
		3. 按提示输入 N 与以逗号分隔的整数列表，程序会输出 while 与 for 两种方法的求和结果。

- `GuessNumber.py`（文件路径：实验四/GuessNumber.py）
	- 运行方式：
			 ```powershell
			 python GuessNumber.py
			 ```
		- 交互示例：
			- 程序生成随机数 N（0-99），用户重复输入直到猜中。

3、运行结果与截图

- 已在 `实验四` 目录生成流程图图片：
	- `Sum_flowchart.png`（Sum 的流程图）
	- `GuessNumber_flowchart.png`（GuessNumber 的流程图）

- 运行示例输出（Sum.py）：
	- 输入：N=5，列表 `1,2,3,4,5` → while 求和结果: 15，for 求和结果: 15

4、实验结果及分析（遇到的问题与解决）

- 问题一：流程图中文显示可能出现乱码
	- 解决：在生成 DOT 时声明 `charset="utf-8"` 并设置 `fontname='Microsoft YaHei'`（或将字体替换为系统已安装的中文字体）；若仍有显示问题，可生成 SVG 在浏览器中查看。

- 问题二：用户输入解析的健壮性
	- 解决：对 N 做整数校验（捕获 ValueError）；解析逗号分隔字符串时去除空项并捕获转换异常，必要时给出友好提示并退出或重试。

5、实验体会

- 本次实验涵盖了基本的输入/输出、循环结构（while/for）、字符串解析与异常处理，以及流程图的程序化生成。通过把流程图脚本化（Graphviz），可以方便地将程序逻辑可视化并嵌入报告中。

附：关键文件列表

- `实验四/Sum.py`  —— while 与 for 两种求和实现
- `实验四/Sum_flowchart.py`  —— 生成 Sum 流程图的脚本
- `实验四/Sum_flowchart.png`  —— 生成的流程图图片
- `实验四/GuessNumber.py`  —— 猜数字程序（学生已完成）
- `实验四/GuessNumber_flowchart.py`  —— 生成 GuessNumber 流程图的脚本
- `实验四/GuessNumber_flowchart.png`  —— 生成的流程图图片

【报告结束】
