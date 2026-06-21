# 给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。 
# 
#  叶子节点 是指没有子节点的节点。 
# 
#  
#  
#  
#  
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# 输出：[[5,4,11,2],[5,8,4,5]]
#  
# 
#  示例 2： 
#  
#  
# 输入：root = [1,2,3], targetSum = 5
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：root = [1,2], targetSum = 0
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点总数在范围 [0, 5000] 内 
#  -1000 <= Node.val <= 1000 
#  -1000 <= targetSum <= 1000 
#  
# 
#  Related Topics 树 深度优先搜索 回溯 二叉树 👍 1248 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        path = []  # 改个更有业务含义的名字
        res = []
        def dfs(node):
            if not node:
                return False
            # 1. 做出选择：把当前节点加入路径
            path.append(node.val)
            # 2. 触发条件：如果是叶子节点，记录一条完整路径
            if not node.left and not node.right and sum(path) == targetSum:
                res.append(list(path))  #这里不加list,小心pop全给你把结果弹没(-_-)

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
