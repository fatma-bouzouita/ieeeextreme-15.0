import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)
t = int(input())
for _ in range(t):
    n, m = [int(i) for i in input().split(" ")]
    arr = []
    for i in range(n):
        s = input()
        p = ['0'] * m
        for j in range(m):
            if s[j] == 'y':
                p[j] = '1'
        arr.append(int("".join(p), 2))
    set_ = set()
    s = 0
    for i in range(n-1):
        mmmm = bin(arr[i])[2:]
        if mmmm.count('0') == 0 and len(mmmm) == m:
            s += int(nCr(n-1, 2))
            continue
        for j in range(i+1, n-1):
            pppp = arr[i] | arr[j]
            pppp = bin(pppp)[2:]
            if pppp.count('0') == 0 and len(pppp) == m:
                s += n-2
                continue
            for k in range(j+1, n):
                p = arr[i] | arr[j] | arr[k]
                p = bin(p)[2:]
                if p.count('0') == 0 and len(p) == m:
                    set_.add(f"{i}{j}{k}")
    print(len(set_)+s)
