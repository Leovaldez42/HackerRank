n = int(input())
arr = []
for arr_i in range(n):
    arr_temp = list(map(int,input().strip().split(' ')))
    arr.append(arr_temp)

d1 = 0
for i in range(n):
    d1 = d1 + arr[i][i]
d2 = 0
for i in range(n):
    d2 = d2 + arr[i][n-i-1]

if d1<d2:
    print(d2-d1)
else:
    print(d1-d2)
