from typing import List
def removeElement(nums, val):
    left = 0
    right = len(nums) - 1

    while left <= right:
        if nums[left] == val:
            # 如果左边是我们要删的，就把最右边的元素挪过来顶包
            nums[left] = nums[right]
            # 右边那个位置已经处理过了（挪走了），所以右边界向内缩
            right -= 1
        else:
            # 如果左边是正常的，就放心跳过，看下一个
            left += 1

    return left

def main():
    return 0
    
if __name__ == '__main__':
    main()