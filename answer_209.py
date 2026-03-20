from typing import List
def minSubArrayLen(target: int, nums: List[int]) -> int:
    res = float('inf')
    my_sum = 0
    slow = 0  # 对应你的 i

    # 标准做法：让右边界 fast (对应你的 tail) 跑在前面
    for fast in range(len(nums)):
        my_sum += nums[fast] # 1. 右边先进一个数

        # 2. 只要够了，就一直缩左边 (对应你那个 while 的反向逻辑)
        while my_sum >= target:
            res = min(res, fast - slow + 1) # 记录当前长度
            my_sum -= nums[slow]           # 踢掉左边的数
            slow += 1                      # 左边界右移

    return res if res != float('inf') else 0


def main():
    nums=[1,2,3,4,5]
    target=12
    res=minSubArrayLen(target,nums)
    print(res)

    
if __name__ == '__main__':
    main()