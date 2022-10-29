from itertools import permutations  

bl = list(map(lambda y: "".join(y), list(permutations(list("*+-/"), 2))))
bl2 = list(map(lambda y: y[0] + '('  + y[1], bl))
t = int(input())
for _ in range(t):
    con = True
    s = input()
    for b in bl:
        if s.find(b) != -1:
            print('invalid')
            con = False
            break
    for b in bl2:
        if s.find(b) != -1:
            print('invalid')
            con = False
            break
    if not con:
        continue
    if (s.find("--") != -1 
    or s.find("**") != -1 
    or s.find('//') != -1 
    or s.find('++') != -1 
    or (not s[0].isdigit() and s[0] != '(')):
        print('invalid')
        continue
    try:
        print(eval(s)%(10**9+7))
    except:
        print('invalid')