n = int(input())

arr = list(map(int, input().rstrip().split()))

a = list(reversed(arr))

#for loop for printing reverse of input
for x in a:
    print(x, end=' ')
