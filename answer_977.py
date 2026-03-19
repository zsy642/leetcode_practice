from typing import List
def sortedSquares(nums: List[int]) -> List[int]:
    nums1=[]
    nums2=[]
    head=0
    tail=len(nums)-1
    while head<=tail:
        if nums[head]<=0:
            nums1.append(nums[head]**2)
            head+=1
        elif nums[tail]>0:
            nums2.append(nums[tail]**2)
            tail-=1
    i=0
    while nums1!=[] and nums2!=[]:
        if nums1[-1]>= nums2[-1]:
            nums[i]=nums2[-1]
            nums2.pop()
        else:
           nums[i]=nums1[-1]
           nums1.pop()
        i+=1
    if nums1==[]:
        nums[i:]=nums2[::-1]
    else:
        nums[i:]=nums1[::-1]
    return nums

def main():
    return 0
    
if __name__ == '__main__':
    main()