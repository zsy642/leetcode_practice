# leetcode submit region begin(Prohibit modification and deletion)
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

def strStr( haystack: str, needle: str) -> int:
    one_next=one_nums(needle)
    j=0
    for i ,v in enumerate(haystack):
        while j>0 and haystack[i]!=needle[j]:
            j=one_next[j-1]
        if haystack[i]==needle[j]:
            j+=1
            if j==len(needle):
                return (i-len(needle)+1)
    return -1
# letcode submit region end(Prohibit modification and deletion)