# 给你一棵 完全二叉树 的根节点 root ，求出该树的节点个数。 
# 
#  完全二叉树 的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层
# 为第 h 层（从第 0 层开始），则该层包含 1~ 2ʰ 个节点。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [1,2,3,4,5,6]
# 输出：6
#  
# 
#  示例 2： 
# 
#  
# 输入：root = []
# 输出：0
#  
# 
#  示例 3： 
# 
#  
# 输入：root = [1]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点的数目范围是[0, 5 * 10⁴] 
#  0 <= Node.val <= 5 * 10⁴ 
#  题目数据保证输入的树是 完全二叉树 
#  
# 
#  
# 
#  进阶：遍历树来统计节点是一种时间复杂度为 O(n) 的简单解决方案。你可以设计一个更快的算法吗？ 
# 
#  Related Topics 位运算 树 二分查找 二叉树 👍 1320 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # 1. 顺着最左边探底，算左深度
        left_depth = 0
        left_node = root
        while left_node:
            left_depth += 1
            left_node = left_node.left

        # 2. 顺着最右边探底，算右深度
        right_depth = 0
        right_node = root
        while right_node:
            right_depth += 1
            right_node = right_node.right

        # 3. 奇迹时刻：如果左右深度一样，说明是满二叉树，直接公式秒杀
        if left_depth == right_depth:
            return (2 ** left_depth) - 1

        # 4. 如果不一样，说明最底层没填满，老老实实：1个根节点 + 左子树节点数 + 右子树节点数
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

        
# leetcode submit region end(Prohibit modification and deletion)
