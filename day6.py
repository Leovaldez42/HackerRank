t = int(input())
for i in range(0,t):
    x = str(input())
    for i in range(0, len(x)):
        if i % 2 == 0:
            print(x[i], end = "")
    print(" ",end = '')

    for j in range(0, len(x)):
        if j % 2 != 0:
            print(x[j], end='')

    print("")
