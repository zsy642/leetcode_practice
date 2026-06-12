# 给你一个二叉树的根节点 root ，按 任意顺序 ，返回所有从根节点到叶子节点的路径。 
# 
#  叶子节点 是指没有子节点的节点。 
# 
#  示例 1： 
#  
#  
# 输入：root = [1,2,3,null,5]
# 输出：["1->2->5","1->3"]
#  
# 
#  示例 2： 
# 
#  
# 输入：root = [1]
# 输出：["1"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点的数目在范围 [1, 100] 内 
#  -100 <= Node.val <= 100 
#  
# 
#  Related Topics 树 深度优先搜索 字符串 回溯 二叉树 👍 1301 👎 0
import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        path = []  # 改个更有业务含义的名字

        def dfs(node):
            if not node:
                return

            # 1. 做出选择：把当前节点加入路径
            path.append(str(node.val))

            # 2. 触发条件：如果是叶子节点，记录一条完整路径
            if not node.left and not node.right:
                res.append('->'.join(path))
                # 注意：这里不需要单独 pop 和 return 了，让它自然往下走
            else:
                # 3. 递归：继续向下探索
                dfs(node.left)
                dfs(node.right)

            # 4. 撤销选择：离开当前节点前，把脚印擦掉
            # 无论是叶子节点还是中间节点，都统一在这里收尾，绝对对称！
            path.pop()

        dfs(root)
        return res
        
# leetcode submit region end(Prohibit modification and deletion)
