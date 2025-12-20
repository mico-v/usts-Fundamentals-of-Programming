import csv
from typing import List, Dict


Record = Dict[str, object]


def _try_parse_float(value: str):
    try:
        return float(value)
    except ValueError:
        return None


def _id_key(id_value: str):
    try:
        return int(id_value)
    except ValueError:
        return id_value


def input_grades(records: List[Record]) -> None:
    print("逐行输入：学号,姓名,数学,语文,英语；空行结束。")
    while True:
        line = input().strip()
        if line == "":
            break
        parts = [p.strip() for p in line.split(",")]
        if len(parts) != 5:
            print("格式错误，应为5个字段：学号,姓名,数学,语文,英语")
            continue
        stu_id, name, math_s, chi_s, eng_s = parts
        math = _try_parse_float(math_s)
        chi = _try_parse_float(chi_s)
        eng = _try_parse_float(eng_s)
        if None in (math, chi, eng):
            print("成绩必须为数字，请重试。")
            continue
        records.append({
            "id": stu_id,
            "name": name,
            "math": math,
            "chinese": chi,
            "english": eng,
        })
    print(f"已输入 {len(records)} 条记录。")


def modify_grade(records: List[Record]) -> None:
    target_id = input("请输入要修改的学生学号：").strip()
    idx = next((i for i, r in enumerate(records) if str(r.get("id")) == target_id), -1)
    if idx == -1:
        print("未找到该学号的学生。")
        return
    print("请输入新的成绩（格式：数学,语文,英语）：")
    line = input().strip()
    parts = [p.strip() for p in line.split(",")]
    if len(parts) != 3:
        print("格式错误，应为3个成绩字段：数学,语文,英语")
        return
    math = _try_parse_float(parts[0])
    chi = _try_parse_float(parts[1])
    eng = _try_parse_float(parts[2])
    if None in (math, chi, eng):
        print("成绩必须为数字。")
        return
    records[idx]["math"] = math
    records[idx]["chinese"] = chi
    records[idx]["english"] = eng
    print("修改完成。")


def query_grade(records: List[Record]) -> None:
    target_id = input("请输入要查询的学生学号：").strip()
    rec = next((r for r in records if str(r.get("id")) == target_id), None)
    if not rec:
        print("未找到该学号的学生。")
        return
    print("查询结果：")
    print(f"学号：{rec['id']}")
    print(f"姓名：{rec['name']}")
    print(f"数学：{rec['math']}")
    print(f"语文：{rec['chinese']}")
    print(f"英文：{rec['english']}")


def output_grades(records: List[Record]) -> None:
    if not records:
        print("暂无成绩。")
        return
    rows = sorted(records, key=lambda r: _id_key(str(r["id"])))
    # 计算列宽
    id_width = max(4, max(len(str(r["id"])) for r in rows))
    name_width = max(2, max(len(str(r["name"])) for r in rows))
    # 表头
    header = (
        f"{'学号'.ljust(id_width)}  "
        f"{'姓名'.ljust(name_width)}  数学    语文    英文"
    )
    print(header)
    print("-" * len(header))
    for r in rows:
        math_str = f"{float(str(r['math'])):.2f}"
        chi_str = f"{float(str(r['chinese'])):.2f}"
        eng_str = f"{float(str(r['english'])):.2f}"
        print(
            f"{str(r['id']).ljust(id_width)}  "
            f"{str(r['name']).ljust(name_width)}  "
            f"{math_str.ljust(6)}  {chi_str.ljust(6)}  {eng_str.ljust(6)}"
        )


def save_grades(records: List[Record], filename: str = "grades.csv") -> None:
    try:
        with open(filename, "w", newline="", encoding="utf-8-sig") as f:
            writer = csv.writer(f)
            writer.writerow(["学号", "姓名", "数学", "语文", "英文"])
            for r in records:
                writer.writerow([
                    r["id"], r["name"], r["math"], r["chinese"], r["english"]
                ])
        print(f"已保存到 {filename}")
    except Exception as e:
        print(f"保存失败：{e}")


def show_menu() -> None:
    print()
    print("1-输入成绩")
    print("2-修改成绩")
    print("3-查询成绩")
    print("4-输出成绩")
    print("5-保存成绩")
    print("0-退出程序")


def main():
    records: List[Record] = []
    while True:
        show_menu()
        choice = input("请选择功能：").strip()
        if choice == "1":
            input_grades(records)
        elif choice == "2":
            modify_grade(records)
        elif choice == "3":
            query_grade(records)
        elif choice == "4":
            output_grades(records)
        elif choice == "5":
            save_grades(records)
        elif choice == "0":
            print("已退出。")
            break
        else:
            print("无效选择，请输入 0-5 之间的数字。")


if __name__ == "__main__":
    main()
