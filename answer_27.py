from typing import List
def removeElement( nums: List[int], val: int) -> int:
    if nums==[]:
        return 0
    i=0
    j=len(nums)-1
    while i!=j:
        if nums[i]==val:
            nums[i],nums[j]=nums[j],nums[i]
            j-=1
        else:
            i+=1
    return i+1 if nums[i]!=val else i
def main():
    return 0
    
if __name__ == '__main__':
    main()