def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    nums=[0]*26
    for i in s:
        index=ord(i)-ord('a')
        nums[index]+=1
    for j in t:
        index=ord(j)-ord('a')
        if nums[index]<=0:
            return False
        nums[index]-=1
    return True
# leetcode submit region end(Prohibit modification and deletion)
