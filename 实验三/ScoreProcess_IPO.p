digraph ScoreProcess {
  rankdir=TB;
  graph [charset="utf-8"];
  node [fontname="Microsoft YaHei", fontsize=12];
  edge [fontname="Microsoft YaHei", fontsize=11];

  start [label="开始", shape=oval];
  input [label="输入成绩 n (0-100)", shape=parallelogram];

  d90  [label="n >= 90?", shape=diamond];
  d80  [label="n >= 80?", shape=diamond];
  d70  [label="n >= 70?", shape=diamond];
  d60  [label="n >= 60?", shape=diamond];

  a_opt [label="输出: 优", shape=rectangle];
  a_good[label="输出: 良", shape=rectangle];
  a_mid [label="输出: 中", shape=rectangle];
  a_pass[label="输出: 及格", shape=rectangle];
  a_fail[label="输出: 不及格", shape=rectangle];

  end [label="结束", shape=oval];

  start -> input -> d90;
  d90 -> a_opt [label="是"];
  d90 -> d80 [label="否"];

  d80 -> a_good [label="是"];
  d80 -> d70 [label="否"];

  d70 -> a_mid [label="是"];
  d70 -> d60 [label="否"];

  d60 -> a_pass [label="是"];
  d60 -> a_fail [label="否"];

  a_opt -> end;
  a_good -> end;
  a_mid -> end;
  a_pass -> end;
  a_fail -> end;
}
