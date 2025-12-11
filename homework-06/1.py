import jieba
import os

base = os.path.dirname(__file__)
tasks = [('红楼梦.txt', '红楼梦人物.txt', '红楼梦_词频.txt'), 
         ('水浒传.txt', '水浒传人物.txt', '水浒传_词频.txt')]

for novel, names, out in tasks:
    with open(os.path.join(base, names), 'r', encoding='utf-8') as f:
        name_list = [line.strip() for line in f if line.strip()]
    
    for name in name_list: jieba.add_word(name)
    
    with open(os.path.join(base, novel), 'r', encoding='utf-8') as f:
        words = jieba.lcut(f.read())
        
    counts = {name: 0 for name in name_list}
    for w in words:
        if w in counts: counts[w] += 1
            
    result = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    
    with open(os.path.join(base, out), 'w', encoding='utf-8') as f:
        for k, v in result: f.write(f"{k} {v}\n")
