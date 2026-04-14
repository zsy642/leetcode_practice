import re
def tool(n):
    res=[]
    for i in range(1, n):
        if i==567:
            res.append(566)
        else:
            res.append(i)
    print("(",res,",",[566,567],'),')

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list2listnode(nums,circle=0,type=0):
    dummy=ListNode(next=nums[0])
    n0=ListNode(nums[0])
    one=n0
    circleone=dummy
    for i in range(0, len(nums)):
        one.next=ListNode(nums[i])
        one=one.next
        if i== circle:
            circleone=one
    if type==1:
        one.next=circleone
    return n0

def listnode2list(head):
    res=[]
    while head:
        res.append(head.val)
        head=head.next
    return res

def test():
    for i in range(1, 1000):
        print(i**0.5)

def testre(num,resnum):
    with open(r'测试原始数据.txt','r',encoding='utf-8') as f:
        text=f.read()
        testtext=r'(	)+(测试用例:)?(.+)\n'*num
        testrule=re.compile(testtext)
        testtexts=testrule.findall(text)
        print(testtexts)
        restext=r'(期望结果:)(.+)'+r'((\n)(.+))+'*(resnum-1)
        resrule=re.compile(restext)
        restexts=resrule.search(text)
        #print(restexts.group(2),restexts.group(5))
        resnum=2
        for i in testtexts:
            tmpstr=f'{i[2]},'
            for j in range (2,num+1):
                tmpstr+=f'{i[3*j-1]},'
            tmpstr+=f'{restexts.group(resnum)})'
            resnum+=3
            print("("+tmpstr+',')

if __name__ == '__main__':
    testre(2,6)
    pass