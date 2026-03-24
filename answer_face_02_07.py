# Definition for singly-linked list.
class ListNode:
    def __init__(self, x=0,next=None):
        self.val = x
        self.next = next


def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    dummy1= ListNode(next=headA)
    dummy2= ListNode(next=headB)
    tail1=dummy1
    tail2=dummy2
    len1=1
    len2=1
    while tail1 and tail1.next:
        tail1=tail1.next
        len1+=1
    while tail2 and tail2.next:
        tail2=tail2.next
        len2+=1
    if tail1 is not tail2:
        return 0
    find1=dummy1
    find2=dummy2
    if len1>=len2:
        for _ in range(len1-len2):
            find1=find1.next
    else:
        for _ in range(len2-len1):
            find2=find2.next
    while find1.next:
        if find1.next is find2.next:
            return find1.next
        find1=find1.next
        find2=find2.next
if __name__=='__main__':
    pass
