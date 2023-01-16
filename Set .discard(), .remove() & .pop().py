n = int(input())
s = set(map(int, input().split()))
t = int(input())
while(t > 0):
    t -= 1
    c = input()
    if c[0] == 'r':
        e = int(c[-1])
        try:
            s.remove(e)
        except:
            pass
    elif c[0] == 'p':
        try:
            s.pop()
        except:
            pass
    elif c[0] == 'd':
        e = int(c[-1])
        s.discard(e)

sum = 0
for i in s:
    sum += i
    
print(sum)