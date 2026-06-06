# 给定一个二叉树： 
# 
#  
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# } 
# 
#  填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL 。 
# 
#  初始状态下，所有 next 指针都被设置为 NULL 。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [1,2,3,4,5,null,7]
# 输出：[1,#,2,3,#,4,5,7,#]
# 解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化输出按层序遍历顺序（由 next 指
# 针连接），'#' 表示每层的末尾。 
# 
#  示例 2： 
# 
#  
# 输入：root = []
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中的节点数在范围 [0, 6000] 内 
#  -100 <= Node.val <= 100 
#  
# 
#  进阶： 
# 
#  
#  你只能使用常量级额外空间。 
#  使用递归解题也符合要求，本题中递归程序的隐式栈空间不计入额外空间复杂度。 
#  
# 
#  
#  
# 
#  Related Topics 树 深度优先搜索 广度优先搜索 链表 二叉树 👍 959 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


'''
大循环改成 而不是most.next
进循环之前lastmost=写一左左存在否则右
进循环之后
先找lastmost，while lastmost，lastmost=写一左左存在否则右，然后current=lastmost
换层小循环mostleft=None
if current.next:current=current.next

如果俩都存在右是lastcurr
current.next=左
current=左
否则左左存在否则右
进循环之后
current.next=lastcurrent
'''


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        curr = root  # 当前层的扫描指针

        while curr:
            # 每一层开局，都新建一个虚拟头节点
            dummy = Node(0)
            tail = dummy  # tail 永远指向下一层当前已经织好网的最后一个节点

            # 开始横向扫描当前层
            while curr:
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next
                if curr.right:
                    tail.next = curr.right
                    tail = tail.next
                curr = curr.next  # 顺着上一层的 next 往右走

            # 当前层走完了，下一层的网已经通过 dummy 织好了
            # dummy.next 就是下一层真正的第一个节点
            curr = dummy.next

        return root

# leetcode submit region end(Prohibit modification and deletion)
