# 给定一个二叉树，判断它是否是 平衡二叉树 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [3,9,20,null,null,15,7]
# 输出：true
#  
# 
#  示例 2： 
#  
#  
# 输入：root = [1,2,2,3,3,null,null,4,4]
# 输出：false
#  
# 
#  示例 3： 
# 
#  
# 输入：root = []
# 输出：true
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中的节点数在范围 [0, 5000] 内 
#  -10⁴ <= Node.val <= 10⁴ 
#  
# 
#  Related Topics 树 深度优先搜索 二叉树 👍 1718 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def finddepth(node):
            if not node:
                return 0

            deepl = finddepth(node.left)
            if deepl == -1: return -1  # 左子树不平衡，立刻熔断

            deepr = finddepth(node.right)
            if deepr == -1: return -1  # 右子树不平衡，立刻熔断

            if abs(deepl - deepr) > 1:
                return -1

            return max(deepl, deepr) + 1

        return finddepth(root) != -1

# leetcode submit region end(Prohibit modification and deletion)
