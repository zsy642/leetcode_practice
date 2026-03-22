from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    while True:
        if not head:
            return None
        if head.val!=val:
            break
        head=head.next
    tmp=head
    while tmp.next:
        if tmp.next.val==val:
            tmp.next=tmp.next.next
        else:
            tmp=tmp.next
    return head



def main():
    no1= ListNode(7)
    no1.next=ListNode(7)
    no1.next.next=ListNode(7)
    no1.next.next.next=ListNode(7)
    res=removeElements(no1, 7)
    print(res)
    
if __name__ == '__main__':
    main()