from typing import List


def fourSum(nums: List[int], target: int) -> List[List[int]]:
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
