from typing import List


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    res=[]
    nums2=set(nums2)
    nums1=set(nums1)
    for x in nums2:
        if x in nums1:
            res.append(x)
    return res
def main():
    nums1=[2,2]
    nums2=[2,2]
    res=intersection(nums1,nums2)
    return 0
    
if __name__ == '__main__':
    main()