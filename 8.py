t = int(input())
for _ in range(t):
    n = int(input())
    s1, s2 = 0, 0
    d1, d2 = 0, 0
    swap = False
    for i in range(n):
        a, b = [int(k) for k in input().split(" ")]
        s1 += a
        s2 += b
        if not swap:
            if a == 6:
                d1 += 1
            if b == 6:
                d2 += 1
        else:
            if b == 6:
                d1 += 1
            if a == 6:
                d2 += 1
        if s1 != s2:
            swap = not swap
    if d1 > d2:
        print("1")
    else:
        print("2")
