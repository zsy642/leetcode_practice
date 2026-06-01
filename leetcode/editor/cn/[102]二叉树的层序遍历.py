# 给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[3],[9,20],[15,7]]
#  
# 
#  示例 2： 
# 
#  
# 输入：root = [1]
# 输出：[[1]]
#  
# 
#  示例 3： 
# 
#  
# 输入：root = []
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数目在范围 [0, 2000] 内 
#  -1000 <= Node.val <= 1000 
#  
# 
#  Related Topics 树 广度优先搜索 二叉树 👍 2308 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q1=deque()
        q2=deque()
        res=[[]]
        use_q = q1
        store_q=q2
        use_q.append(root)
        while q1 or q2:
            if not use_q:
                res.append([])
                use_q,store_q=store_q,use_q
            tmp=use_q.popleft()
            if tmp : res[-1].append(tmp.val)
            if tmp.left: store_q.append(tmp.left)
            if tmp.right: store_q.append(tmp.right)
        return res


# leetcode submit region end(Prohibit modification and deletion)
