n = int(input())
arr = list(map(int, input().strip().split()))
x = 0
y = 0
z = 0
n = len(arr)
for i in range(0,n):
    if arr[i] > 0:
        x += 1
    if arr[i] < 0:
        y += 1
    if arr[i] == 0:
        z += 1

print(float(x/n))
print(float(y/n))
print(float(z/n))
