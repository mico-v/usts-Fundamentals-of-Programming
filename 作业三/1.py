M = 60
up = 0.5
m =0
for i in range(10):
    M += up
    m = M*0.165
    print(f"第{i}年在地球上重{M:.2f}kg,在月球上重{m:.2f}kg")
