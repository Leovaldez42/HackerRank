arr = list(map(int, input().rstrip().split()))
arr.sort()
print(str(int(sum(arr))-int(arr[-1])) + " " + str(int(sum(arr))-int(arr[0])))
