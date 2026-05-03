from collections import deque
def maxSlidingWindow(nums, k: int) :
    queque = deque()
    maybe = deque()
    maybe_i = deque()
    maybe.append(float('-inf'))
    maybe_i.append(-3.14)
    res = []
    for i, value in enumerate(nums):
        if len(queque) <= k:
            queque.append(value)
            while maybe!=deque() and value >= maybe[-1]:
                maybe.pop()
                maybe_i.pop()
            maybe.append(value)
            maybe_i.append(i)
            if maybe_i[0] < (i - k + 1):
                maybe.popleft()
                maybe_i.popleft()
        if len(queque) >= k:
            res.append(maybe[0])
            queque.popleft()
    return res