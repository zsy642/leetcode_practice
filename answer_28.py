
def strStr(haystack: str, needle: str) -> int:
    s=needle[0]
    index=-1
    for i in range(len(haystack)):
        if haystack[i]==s:
            index=i
            for j in needle:
                if index>(len(haystack)-1) or j !=haystack[index]:
                    index=-1
                    break
                index+=1
            if index!=-1:
                return i

