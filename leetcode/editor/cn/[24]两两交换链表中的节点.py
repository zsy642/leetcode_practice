# 给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：head = [1,2,3,4]
# 输出：[2,1,4,3]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = []
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：head = [1]
# 输出：[1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点的数目在范围 [0, 100] 内 
#  0 <= Node.val <= 100 
#  
# 
#  Related Topics 递归 链表 👍 2580 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swap(past):
    staff=past.next
    past.next=past.next.next
    staff.next=staff.next.next
    past.next.next=staff

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummy=ListNode(next=head)
        tmp=dummy
        while tmp.next.next:
            swap(tmp)
            tmp=tmp.next.next
            if not tmp.next:
                break
        return dummy.next


        
# leetcode submit region end(Prohibit modification and deletion)
