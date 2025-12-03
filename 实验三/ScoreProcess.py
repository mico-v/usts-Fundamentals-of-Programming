# 1、成绩处理。
# 编写一个Python程序ScoreProcess.py，
# 用户从键盘输入一个100内的某门课程的成绩，
# 程序将其他转换为五级记分（优、良、中、及格、不及格）并输出。


n = int(input("请输入成绩"))

if n>=90:
    ans = "优"
elif n>=80:
    ans = "良"
elif n>=70:
    ans = "中"
elif n>=60:
    ans = "及格"
else:
    ans = "不及格"

print(ans)