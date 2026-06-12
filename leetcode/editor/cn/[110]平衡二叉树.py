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
        #checkBalanced(root)-> int #返回值 返回一边的高度
            #获取左右的高度
            #如果绝对值>1直接返回999
            #否则继续向上递归
        #调用checkBalaned,如果小于
        if not root:
            return True
            # finddepth形参节点,返回值深度(算自己也算叶子)和底层叶子数

        def finddepth(root):
            # 退出条件如果是叶子返回1如果是一个叶子返回2
            if not root:
                return 0
            if not root.left and not root.right:
                return 1

            # 每次先左调用一次,判断没有叶子再进行右边调用,否则直接返回高度和叶子数
            deepl = finddepth(root.left)
            deepr = finddepth(root.right)
            if  deepl==-1 or deepr==-1:
                return -1
            if abs(deepl-deepr)>1:
                return -1
            return max(deepl,deepr) + 1

        if (finddepth(root))==-1:
            return False
        else:
            return True

# leetcode submit region end(Prohibit modification and deletion)
