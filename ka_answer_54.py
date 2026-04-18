import sys
s=sys.stdin. read().split()[0]
s=list(s)
l=len(s)
ex=0
for i in s:
    if i>='0' and i<='9':
        ex+=5
for _ in range(ex):
    s.append('a')
tail=l+ex-1
head=l-1
while head<tail:
    if '0' <= s[head] <= '9':
        s[tail-5:tail+1]=['n','u','m','b','e','r']
        tail-=6
    else :
        s[tail]=s[head]
        tail-=1
    head-=1
s=''.join(s)
print(s)