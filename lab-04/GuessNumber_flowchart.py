"""生成 GuessNumber.py 的流程图并输出 PNG（需安装 graphviz）
运行: python GuessNumber_flowchart.py
输出: GuessNumber_flowchart.png
"""
from graphviz import Digraph


def make_flowchart(output_path='GuessNumber_flowchart'):
    g = Digraph(format='png')
    g.graph_attr['charset'] = 'utf-8'
    g.node_attr.update(fontname='Microsoft YaHei', fontsize='12')
    g.edge_attr.update(fontname='Microsoft YaHei', fontsize='11')
    g.attr(rankdir='TB')

    g.node('start', '开始', shape='oval')
    g.node('gen', '生成随机数 N (0-99)', shape='rectangle')
    g.node('input', '输入一个整数 (0-99)', shape='parallelogram')
    g.node('try_parse', '尝试转换为整数 (int)', shape='rectangle')
    g.node('invalid', '输入非整型\n打印错误并回到输入', shape='rectangle')
    g.node('inc', 'count += 1', shape='rectangle')
    g.node('cmp1', 'n > N ?', shape='diamond')
    g.node('too_big', '打印: 遗憾，太大了', shape='rectangle')
    g.node('cmp2', 'n < N ?', shape='diamond')
    g.node('too_small', '打印: 遗憾，太小了', shape='rectangle')
    g.node('success', '打印: 猜中并退出', shape='parallelogram')
    g.node('end', '结束', shape='oval')

    g.edge('start', 'gen')
    g.edge('gen', 'input')
    g.edge('input', 'try_parse')
    g.edge('try_parse', 'invalid', label='异常')
    g.edge('invalid', 'input')
    g.edge('try_parse', 'inc', label='成功')
    g.edge('inc', 'cmp1')
    g.edge('cmp1', 'too_big', label='是')
    g.edge('too_big', 'input')
    g.edge('cmp1', 'cmp2', label='否')
    g.edge('cmp2', 'too_small', label='是')
    g.edge('too_small', 'input')
    g.edge('cmp2', 'success', label='否')
    g.edge('success', 'end')

    g.render(output_path, view=False)


if __name__ == '__main__':
    make_flowchart()
