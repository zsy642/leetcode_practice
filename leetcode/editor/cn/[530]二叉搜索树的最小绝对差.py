# 给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。 
# 
#  差值是一个正数，其数值等于两值之差的绝对值。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [4,2,6,1,3]
# 输出：1
#  
# 
#  示例 2： 
#  
#  
# 输入：root = [1,0,48,null,null,12,49]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点的数目范围是 [2, 10⁴] 
#  0 <= Node.val <= 10⁵ 
#  
# 
#  
# 
#  注意：本题与 783 https://leetcode.cn/problems/minimum-distance-between-bst-nodes/ 相
# 同 
# 
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉搜索树 二叉树 👍 669 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.lastnum=float('-inf')
        result=float('inf')
        def MinimumDifference(root):
            if root== None:
                return
            MinimumDifference(root.left)
            nonlocal result
            result=min(result,root.val-self.lastnum)
            self.lastnum=root.val
            MinimumDifference(root.right)
        MinimumDifference(root)
        return result
        
# leetcode submit region end(Prohibit modification and deletion)
