import sys
def solve():
    # 读取所有输入，按空格切分
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    # 比如第一行是 target，第二行是 n
    n = int(input_data[0])
    # 剩下的就是数组元素
    nums = [int(x) for x in input_data[1:n+1]]
    for i in range(1,n):
        nums[i]+=nums[i-1]
    for tmp in range(n+1,len(input_data)-1,2):
        start=int(input_data[tmp])
        over=int(input_data[tmp+1])
        res=nums[over]-(nums[start-1] if (start-1)>=0 else 0)
        print(res)
if __name__ == "__main__":
    solve()