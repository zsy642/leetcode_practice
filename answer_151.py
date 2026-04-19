def reverseWords(s: str) -> str:
    s=s.strip()
    s=list(s)
    tmp=''
    head=0
    tail=0
    real=0
    s=s[::-1]
    while head<len(s):
        tail+=1
        if tail==len(s) or s[tail]==' ':
            if head!=0:
                s[real:real+tail-head]=s[tail-1:head-1:-1]
            else:
                s[real:real+tail-head]=s[tail-1::-1]
            if tail<=len(s)-1:
                s[real+tail-head]=' '
            real+=(tail-head+1)
            while tail<len(s)-1 and s[tail]==' ':
                tail+=1
            head=tail
    s=s[0:real+tail-head-1]
    s=''.join(s)
    return s


