from typing import Optional

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy=ListNode(next=head)
    target1=dummy
    for _ in range(n):
        target1=target1.next
    target2=dummy
    while target1.next:
        target1=target1.next
        target2=target2.next
    target2.next=target2.next.next
    return dummy.next
if __name__=='__main__':
    pass