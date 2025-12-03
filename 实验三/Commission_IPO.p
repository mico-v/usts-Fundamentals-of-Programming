digraph Commission {
  rankdir=TB;
  graph [charset="utf-8"];
  node [fontname="Microsoft YaHei", fontsize=12];
  edge [fontname="Microsoft YaHei", fontsize=11];
  start [label="开始", shape=oval];
  input [label="输入当月利润 I", shape=parallelogram];
  proc_init [label="P = 0\nIt=[0,10,20,40,60,100]\nCent=[0.1,0.075,0.05,0.03,0.015,0.01]", shape=rectangle];
  init_i [label="i = 5", shape=rectangle];

  check_i [label="i >= 0?", shape=diamond];
  check_cmp [label="I > It[i]?", shape=diamond];
  calc_M [label="M = I - It[i]", shape=rectangle];
  update_P [label="P += M * Cent[i]", shape=rectangle];
  update_I [label="I -= M", shape=rectangle];
  dec_i [label="i = i - 1", shape=rectangle];

  out [label="输出: 应发放奖金 P", shape=parallelogram];
  end [label="结束", shape=oval];

  start -> input -> proc_init -> init_i -> check_i;
  check_i -> check_cmp [label="是"];
  check_i -> out [label="否"];

  check_cmp -> calc_M [label="是"];
  check_cmp -> dec_i [label="否"];

  calc_M -> update_P -> update_I -> dec_i;
  dec_i -> check_i;

  out -> end;
}
