# leetcode submit region begin(Prohibit modification and deletion)
def one_nums(s):
    l=len(s)
    one_next=[0]*l
    j=0
    for i in range(1,len(s)):
        if j>0 and s[i]!=s[j]:
            j=one_next[j-1]
        if s[i]==s[j]:
            j+=1
            one_next[i]=j
    return one_next
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        one_next=one_nums(needle)
        j=0
        i=0
        while i<len(haystack):
            if haystack[i]==needle[j]:
                j+=1
                i+=1
                if j==len(needle):
                    return (i-len(needle))
            else:
                if j==0:
                    i+=1
                else:
                    j=one_next[j-1]
        return -1

# leetcode submit region end(Prohibit modification and deletion)

