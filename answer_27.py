from typing import List
def removeElement( nums: List[int], val: int) -> int:
    try:
        while True:
            nums.remove(val)
    except ValueError:
        return len(nums)
def main():
    return 0
    
if __name__ == '__main__':
    main()