# 给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[
# b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）： 
# 
#  
#  0 <= a, b, c, d < n 
#  a、b、c 和 d 互不相同 
#  nums[a] + nums[b] + nums[c] + nums[d] == target 
#  
# 
#  你可以按 任意顺序 返回答案 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,0,-1,0,-2,2], target = 0
# 输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [2,2,2,2,2], target = 8
# 输出：[[2,2,2,2]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 200 
#  -10⁹ <= nums[i] <= 10⁹ 
#  -10⁹ <= target <= 10⁹ 
#  
# 
#  Related Topics 数组 双指针 排序 👍 2165 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        d=0
        while d<=(len(nums)-1):
            b=d+1
            while b<=(len(nums)-1):
                a=b+1
                c=len(nums)-1
                while a<c:
                    if nums[a]+nums[b]+nums[c]+nums[d]==target:
                        res.append([nums[a],nums[b],nums[c],nums[d]])
                        c-=1
                        while (c<(len(nums)-1)and c>=0) and nums[c+1]==nums[c]:
                            c-=1
                    elif nums[a]+nums[b]+nums[c]+nums[d]>target:
                        c-=1
                    else:
                        a+=1
                b+=1
                while (b<len(nums)) and nums[b-1]==nums[b]:
                    b+=1
            d+=1
            while (d<len(nums)) and nums[d-1]==nums[d]:
                d+=1
        return res
# leetcode submit region end(Prohibit modification and deletion)
