# 给定一个二叉树 root ，返回其最大深度。 
# 
#  二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 
#  
# 输入：root = [3,9,20,null,null,15,7]
# 输出：3
#  
# 
#  示例 2： 
# 
#  
# 输入：root = [1,null,2]
# 输出：2
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点的数量在 [0, 10⁴] 区间内。 
#  -100 <= Node.val <= 100 
#  
# 
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 2119 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

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

            res.append(current_level)

        return len(res)
# leetcode submit region end(Prohibit modification and deletion)
