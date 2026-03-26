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

if __name__ == '__main__':
    pass