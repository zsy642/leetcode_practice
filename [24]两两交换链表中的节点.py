from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swap(past):
    work=past
    staff=past.next
    past.next=past.next.next
    staff.next=staff.next.next
    work.next.next=staff


def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
    dummy=ListNode(next=head)
    tmp=dummy
    while tmp.next and tmp.next.next:
        swap(tmp)
        tmp=tmp.next.next
    return dummy.next

def main():
    n0=ListNode(val=1)
    n0.next=ListNode(val=2)
    n0.next.next=ListNode(val=3)
    n0.next.next.next=ListNode(val=4)
    res= swapPairs(n0)
    print(res)
    return 0
    
if __name__ == '__main__':
    main()