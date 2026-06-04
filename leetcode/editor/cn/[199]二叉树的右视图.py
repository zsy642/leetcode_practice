# 给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。 
# 
#  
# 
#  示例 1： 
# 
#  
#  输入：root = [1,2,3,null,5,null,4] 
#  
# 
#  输出：[1,3,4] 
# 
#  解释： 
# 
#  
# 
#  示例 2： 
# 
#  
#  输入：root = [1,2,3,4,null,null,null,5] 
#  
# 
#  输出：[1,3,4,5] 
# 
#  解释： 
# 
#  
# 
#  示例 3： 
# 
#  
#  输入：root = [1,null,3] 
#  
# 
#  输出：[1,3] 
# 
#  示例 4： 
# 
#  
#  输入：root = [] 
#  
# 
#  输出：[] 
# 
#  
# 
#  提示: 
# 
#  
#  二叉树的节点个数的范围是 [0,100] 
#  
#  -100 <= Node.val <= 100 
#  
# 
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 1335 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque([root])  # 只需要一个队列
        res = []

        while queue:
            level_size = len(queue)  # 关键：拍个快照，记录当前层有多少个节点
            current_level = []

            # 这个 for 循环雷打不动，只消费当前层的数量
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)

                # 悄悄把下一层的节点推进队列尾部，绝不影响本次循环
                if node.left:  queue.append(node.left)
                if node.right: queue.append(node.right)

            res.append(current_level[-1])

        return res
# leetcode submit region end(Prohibit modification and deletion)
