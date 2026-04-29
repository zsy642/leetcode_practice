def one_nums(s):
    l=len(s)
    one_next=[0]*l
    j=0
    for i in range(1,len(s)):
        while j>0 and s[i]!=s[j]:
            j=one_next[j-1]
        if s[i]==s[j]:
            j+=1
            one_next[i]=j
    return one_next

def repeatedSubstringPattern( s: str) -> bool:
    if len(s)==1:
        return False
    one_next=one_nums(s)
    rel=len(s)-one_next[-1]
    if one_next[-1]>=rel and one_next[-1]%rel==0:
        return True
    else:
        return False