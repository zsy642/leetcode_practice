import sys
def solve():
    #---------处理输入-----------
    sys.stdin = open('input.txt', 'r')
    data=sys.stdin.read().split()
    if not data:
        return
    row=int(data[0])
    column=int(data[1])
    #---------获取行列和数组--------------------
    rows=[0]*row
    columns=[0]*column
    for m in range(row):
        for n in range(column):
            rows[m]+=int(data[2+m*column+n])

    for n in range(column):
        for m in range(row):
            columns[n]+=int(data[2+n+m*column])
    #----------获取行列前缀和数组-----------------
    def nums_sum(nums):
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        return nums
    rows=nums_sum(rows)
    columns=nums_sum(columns)
    #------------计算并打印返回结果-----------
    res=float('inf')
    for i in range(len(rows)):
        res=min(res,abs(rows[i]*2-rows[-1]))
    for i in range(len(columns)):
        res=min(res,abs(columns[i]*2-columns[-1]))
    print(res)
    return res

if __name__ == '__main__':
    solve()