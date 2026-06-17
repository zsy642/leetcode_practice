# 给定一个二叉树的 根节点 root，请找出该二叉树的 最底层 最左边 节点的值。 
# 
#  假设二叉树中至少有一个节点。 
# 
#  
# 
#  示例 1: 
# 
#  
# 
#  
# 输入: root = [2,1,3]
# 输出: 1
#  
# 
#  示例 2: 
# 
#  
# 
#  
# 输入: [1,2,3,4,null,5,6,null,null,7]
# 输出: 7
#  
# 
#  
# 
#  提示: 
# 
#  
#  二叉树的节点个数的范围是 [1,10⁴] 
#  
#  -2³¹ <= Node.val <= 2³¹ - 1 
#  
# 
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 661 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # res 存 (节点值, 最大深度)
        # 初始深度给 1，因为 root 必然存在（题目给出了不为空的限制）
        res = (root.val, 1)

        def dfs(node, depth):
            nonlocal res
            if not node:
                return

            # 中：如果是叶子节点，且破了深度纪录，直接占坑
            if not node.left and not node.right:
                if depth > res[1]:
                    res = (node.val, depth)

            # 左、右：下钻时直接把 depth + 1 传下去，不改变当前层的 depth
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 1)
        return res[0]
# leetcode submit region end(Prohibit modification and deletion)
