from typing import List
def minSubArrayLen( target: int, nums: List[int]) -> int:
    #-------------判定能否完成任务-----------
    judge=[x for x in nums if x>0]
    total=sum(judge)
    if total< target:
        return 0
    #----------初始化,并获取基础和与结果------------
    my_sum=0
    flag=True
    tail=0
    while my_sum<target:
        if tail==len(nums) and my_sum<target:
            break
        my_sum+=nums[tail]
        tail+=1
    res=length=tail
    #-------------循环比较-----------------------
    for i in range(1,len(nums)):
        my_sum-=nums[i-1]
        length-=1
        while my_sum<target:
            if tail==len(nums) and my_sum<target:
                flag=False
                break
            my_sum+=nums[tail]
            tail+=1
            length+=1
            flag=True
        if flag:
            res=min(res,length)
    return max(res,1)


def main():
    nums=[1,2,3,4,5]
    target=12
    res=minSubArrayLen(target,nums)
    print(res)

    
if __name__ == '__main__':
    main()