digraph Palindrome {
  rankdir=TB;
  graph [charset="utf-8"];
  node [fontname="Microsoft YaHei", fontsize=12];
  edge [fontname="Microsoft YaHei", fontsize=11];
  start [label="开始", shape=oval];
  input [label="输入字符串 n", shape=parallelogram];
  init_ans [label="ans = True", shape=rectangle];
  calc_half [label="half = len(n)//2", shape=rectangle];
  init_i [label="i = 0", shape=rectangle];

  check_i [label="i < half?", shape=diamond];
  compare [label="n[i] == n[-i-1]?", shape=diamond];
  set_false [label="ans = False", shape=rectangle];
  inc_i [label="i = i + 1", shape=rectangle];

  out_yes [label="输出: 是回文数", shape=parallelogram];
  out_no  [label="输出: 不是回文数", shape=parallelogram];
  end [label="结束", shape=oval];

  start -> input -> init_ans -> calc_half -> init_i -> check_i;
  check_i -> compare [label="是"];
  check_i -> out_yes [label="否"];

  compare -> inc_i [label="是"];
  compare -> set_false [label="否"];

  inc_i -> check_i;
  set_false -> out_no -> end;
  out_yes -> end;
}
