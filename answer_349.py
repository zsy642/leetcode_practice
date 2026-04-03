from typing import List


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    return list(set(nums1) & set(nums2))# & 是集合交集运算，底层全是哈希
def main():
    nums1=[2,2]
    nums2=[2,2]
    res=intersection(nums1,nums2)
    return 0
    
if __name__ == '__main__':
    main()