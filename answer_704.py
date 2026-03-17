from typing import List

def search(nums: List[int], target: int) -> int:
    left=0
    right=len(nums)-1
    while right>=left:
        mid=(left+right)//2
        if nums[mid]>target:
            right=mid-1
        elif nums[mid]<target:
            left=mid+1
        else:
            return mid
    return -1



def main():
    return 0
if __name__ == '__main__':
    main()