from typing import List
def removeElement(nums, val):
    slow=0
    fast=0
    for num in nums:
        if num!=val:
            nums[slow]=num
            slow+=1
    return slow

def main():
    return 0
    
if __name__ == '__main__':
    main()