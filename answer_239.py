from collections import deque


def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    # 只要这一个“砖头”就够了，存索引
    dq = deque()
    res = []

    for i, val in enumerate(nums):
        # 1. 谁比我弱，谁就走（保持单调递减）
        while dq and nums[dq[-1]] <= val:
            dq.pop()
        dq.append(i)

        # 2. 谁太老了，谁就走（判断索引是否过期）
        if dq[0] == i - k:
            dq.popleft()

        # 3. 窗口成型，记录老大
        if i >= k - 1:
            res.append(nums[dq[0]])

    return res