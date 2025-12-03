"""生成 Sum 程序的流程图（使用 graphviz）
需要：pip install graphviz 且系统安装 Graphviz 可执行程序（dot）

运行：python Sum_flowchart.py
这会在同一目录生成 Sum_flowchart.png
"""
from graphviz import Digraph


def make_flowchart(output_path='Sum_flowchart'):
    g = Digraph(format='png')
    g.graph_attr['charset'] = 'utf-8'
    g.node_attr.update(fontname='Microsoft YaHei', fontsize='12')
    g.edge_attr.update(fontname='Microsoft YaHei', fontsize='11')
    g.attr(rankdir='TB')

    g.node('start', '开始', shape='oval')
    g.node('read_n', '输入元素个数 N', shape='parallelogram')
    g.node('check_n', 'N 为正整数?', shape='diamond')
    g.node('read_list', '输入 N 个整数（逗号分隔）', shape='parallelogram')

    g.node('parse', '解析为整数列表', shape='rectangle')

    # while 部分
    g.node('init_i', 'i=0; total1=0', shape='rectangle')
    g.node('cond_while', 'i < len(nums) and i < N ?', shape='diamond')
    g.node('add_while', 'total1 += nums[i]; i += 1', shape='rectangle')

    # for 部分
    g.node('for_loop', 'for x in nums[:N]: total2 += x', shape='rectangle')

    g.node('print', '输出两个结果', shape='parallelogram')
    g.node('end', '结束', shape='oval')

    # 边
    g.edge('start', 'read_n')
    g.edge('read_n', 'check_n')
    g.edge('check_n', 'read_list', label='是')
    g.edge('check_n', 'end', label='否')
    g.edge('read_list', 'parse')

    g.edge('parse', 'init_i')
    g.edge('init_i', 'cond_while')
    g.edge('cond_while', 'add_while', label='是')
    g.edge('add_while', 'cond_while')
    g.edge('cond_while', 'for_loop', label='否')

    g.edge('for_loop', 'print')
    g.edge('print', 'end')

    g.render(output_path, view=False)


if __name__ == '__main__':
    make_flowchart()
