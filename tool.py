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

def list2listnode(nums):
    n0=ListNode(nums[0])
    one=n0
    for i in range(1, len(nums)):
        one.next=ListNode(nums[i])
        one=one.next
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