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
    for i in range(n-1):
        for j in range(i+1, n-1):
            if i == j:
                continue
            for k in range(j+1, n):
                if k == i or k == j:
                    continue
                p = arr[i] | arr[j] | arr[k]
                p = bin(p)[2:]
                if p.count('0') == 0 and len(p) == m:
                    set_.add(f"{i}{j}{k}")
    print(len(set_))
