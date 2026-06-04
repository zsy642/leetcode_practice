# 给定一个二叉树，找出其最小深度。 
# 
#  最小深度是从根节点到最近叶子节点的最短路径上的节点数量。 
# 
#  说明：叶子节点是指没有子节点的节点。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [3,9,20,null,null,15,7]
# 输出：2
#  
# 
#  示例 2： 
# 
#  
# 输入：root = [2,null,3,null,4,null,5,null,6]
# 输出：5
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数的范围在 [0, 10⁵] 内 
#  -1000 <= Node.val <= 1000 
#  
# 
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 1343 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    def minDepth(self, root: Optional[TreeNode]) -> int:
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
                if not node.left and not node.right:
                    break
                if node.left:  queue.append(node.left)
                if node.right: queue.append(node.right)

            res.append(current_level)
            if not node.left and not node.right:
                break

        return len(res)
# leetcode submit region end(Prohibit modification and deletion)
