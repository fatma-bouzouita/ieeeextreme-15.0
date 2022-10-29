p, q, n, m = [int(i) for i in input().split(" ")]
s = 0
for i in range(1, n+1):
    s += pow(p, i, m) * pow(i, q, m)
print(s % m)