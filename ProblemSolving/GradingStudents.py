for i in range(0, int(input())):
    m = int(input())

    if m < 38:
        m = m
    
    if m >= 38:
        r = m % 5
        if r == 3:
            m = m + 2
        elif r == 4:
            m = m + 1
        else:
            m = m

    print(m)
