arr = []
for arr_i in range(6):
    arr_temp = list(map(int,input().strip().split(' ')))
    arr.append(arr_temp)

res = 0

for x in range(0,4):
    for y in range(0,4):
        s = sum(arr[x][y:y+3]) + arr[x+1][y+1] + sum([x+2][y:y+3])
        res.append(s)

print(max(res))
