def reverseWords(s: str) -> str:
    s=s.strip()
    s=list(s)
    tmp=''
    new_s=[]
    for i in range(len(s)-1,-1,-1):
        if s[i]==' ':
            if tmp:
                new_s.append(tmp[::-1])
            tmp=''
        else:
            tmp+=s[i]
    new_s.append(tmp[::-1])
    new_s=' '.join(new_s)
    return new_s

