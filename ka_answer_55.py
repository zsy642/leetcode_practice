import sys


def abbb(s,target):
    #import sys
    #date=sys.stdin.read().split()
    #target=int(date[0])
    s=list(s)
    #s=list(date[1])
    o=len(s)-1
    h=o-target
    i=0 #
    while h>-1:
        s[h],s[o]=s[o],s[h]
        h-=1
        o-=1
        i+=1
    h=i%target-1
    while o>0 and (len(s)%target !=0):
        s[h],s[o]=s[o],s[h]
        h=abs((h-1)%(i%target))
        o-=1
    s=''.join(s)
    return s

if __name__ == '__main__':
    main()