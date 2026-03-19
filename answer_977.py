from typing import List
def sortedSquares(nums: List[int]) -> List[int]:
    head=0
    tail=len(nums)-1
    new_nums=[None]*len(nums)
    new_tail=len(nums)-1
    while head<=tail:
        if nums[head]**2>=nums[tail]**2:
            new_nums[new_tail]=nums[head]**2
            head+=1
        else :
            new_nums[new_tail]=nums[tail]**2
            tail-=1
        new_tail-=1
    return new_nums

def main():
    return 0
    
if __name__ == '__main__':
    main()