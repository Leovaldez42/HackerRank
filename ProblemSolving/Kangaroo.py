l = list(map(int, input("").split(" ")))
x1 = l[0]
v1 = l[1]
x2 = l[2]
v2 = l[3]
count = 0
for i in range(0, 10000):
    if x1 + i*v1 == x2 + i*v2:
        print("YES")
        count = 1
        break
if count == 0:
    print("NO")
