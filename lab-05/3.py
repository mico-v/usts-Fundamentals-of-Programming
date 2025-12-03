# 3. 字典应用
# (1) 创建一个字典Student，描述学生基本信息个人，包括学号ID(不能用id)、姓名Name、就读学校University
Student = {
    'ID': '2023001',
    'Name': '张三',
    'University': '苏州科技大学'
}
print("初始字典:", Student)
# 输出: 初始字典: {'ID': '2023001', 'Name': '张三', 'University': '苏州科技大学'}

# (2) 新增字典项年级Grade
Student['Grade'] = '大二'
print("新增年级后:", Student)
# 输出: 新增年级后: {'ID': '2023001', 'Name': '张三', 'University': '苏州科技大学', 'Grade': '大二'}

# (3) 分别用字典对象的items()、keys()、values()函数，并显示字典对象中的所有信息
print("Items:", list(Student.items()))
# 输出: Items: [('ID', '2023001'), ('Name', '张三'), ('University', '苏州科技大学'), ('Grade', '大二')]
print("Keys:", list(Student.keys()))
# 输出: Keys: ['ID', 'Name', 'University', 'Grade']
print("Values:", list(Student.values()))
# 输出: Values: ['2023001', '张三', '苏州科技大学', '大二']

print("遍历信息:")
# 输出: 遍历信息:
for k, v in Student.items():
    print(f"{k}: {v}")
# 输出:
# ID: 2023001
# Name: 张三
# University: 苏州科技大学
# Grade: 大二

# (4) 删除字典对象中的“就读学校university”
if 'University' in Student:
    del Student['University']
print("删除学校后:", Student)
# 输出: 删除学校后: {'ID': '2023001', 'Name': '张三', 'Grade': '大二'}
