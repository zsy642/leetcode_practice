from collections import deque
def topKFrequent(nums, k: int):
    tmp = {}
    res = []
    one_num=0
    for value in nums:
        tmp[value] = tmp.get(value, 0) + 1
    startque = [] * len(tmp)
    for i in tmp:
        startque.append(i)
        tmpp=one_num
        while tmpp and tmp[i] < tmp[startque[tmpp-1]]:
            startque[tmpp],startque[tmpp-1]=startque[tmpp-1],startque[tmpp]
            tmpp-=1
        one_num += 1
    return startque[len(startque)-k::]