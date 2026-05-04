from collections import deque
def topKFrequent(nums, k: int):
    tmp = {}
    for value in nums:
        tmp[value] = tmp.get(value, 0) + 1
    sorted_by_value = dict(sorted(tmp.items(), key=lambda item: item[1],reverse=True))
    res=list(sorted_by_value)
    return res[0:k]