records=[]
while True:
    print("\n1-输入成绩\n2-修改成绩\n3-查询成绩\n4-输出成绩\n5-保存成绩\n0-退出程序")
    c=input("请选择功能：").strip()
    if c=="1":
        print("逐行输入：学号,姓名,数学,语文,英语；空行结束。")
        while True:
            s=input().strip()
            if not s: break
            i,n,m,chi,e=[x.strip() for x in s.split(",")]
            records.append({"id":i,"name":n,"math":float(m),"chi":float(chi),"eng":float(e)})
    elif c=="2":
        t=input("请输入要修改的学生学号：").strip()
        r=next((x for x in records if x["id"]==t),None)
        if not r: print("未找到该学号的学生。"); continue
        m,chi,e=[x.strip() for x in input("请输入新的成绩（数学,语文,英语）：").split(",")]
        r["math"]=float(m); r["chi"]=float(chi); r["eng"]=float(e); print("修改完成。")
    elif c=="3":
        t=input("请输入要查询的学生学号：").strip()
        r=next((x for x in records if x["id"]==t),None)
        if not r: print("未找到该学号的学生。"); continue
        print("学号：",r["id"]); print("姓名：",r["name"])
        print("数学：",r["math"]); print("语文：",r["chi"]); print("英文：",r["eng"])
    elif c=="4":
        if not records: print("暂无成绩"); continue
        rows=sorted(records,key=lambda x:int(x["id"]))
        print("学号 姓名 数学 语文 英文")
        for r in rows:
            print(r["id"],r["name"],f"{r['math']:.2f}",f"{r['chi']:.2f}",f"{r['eng']:.2f}")
    elif c=="5":
        import csv
        with open("grades.csv","w",newline="",encoding="utf-8-sig") as f:
            w=csv.writer(f); w.writerow(["学号","姓名","数学","语文","英文"])
            w.writerows((r["id"],r["name"],r["math"],r["chi"],r["eng"]) for r in records)
        print("已保存到 grades.csv")
    elif c=="0":
        print("已退出。"); break
    else:
        print("无效选择，请输入 0-5 之间的数字。")