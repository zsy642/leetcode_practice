# 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。 
# 
#  有效 二叉搜索树定义如下： 
# 
#  
#  节点的左子树只包含 严格小于 当前节点的数。 
#  节点的右子树只包含 严格大于 当前节点的数。 
#  所有左子树和右子树自身必须也是二叉搜索树。 
#  
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [2,1,3]
# 输出：true
#  
# 
#  示例 2： 
#  
#  
# 输入：root = [5,1,4,null,null,3,6]
# 输出：false
# 解释：根节点的值是 5 ，但是右子节点的值是 4 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数目范围在[1, 10⁴] 内 
#  -2³¹ <= Node.val <= 2³¹ - 1 
#  
# 
#  Related Topics 树 深度优先搜索 二叉搜索树 二叉树 👍 2783 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        magic=float('inf')
        res = float('-inf')
        def dfs(root):
            nonlocal res
            if not root:
                return
            if dfs(root.left)==magic:
                return magic
            if res == magic:
                return magic
            res=root.val if root.val>res else magic
            if dfs(root.right)==magic:
                return magic

        dfs(root)
        return False if res == magic else True
# leetcode submit region end(Prohibit modification and deletion)
