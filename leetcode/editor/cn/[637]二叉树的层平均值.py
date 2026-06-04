# 给定一个非空二叉树的根节点
#  root , 以数组的形式返回每一层节点的平均值。与实际答案相差 10⁻⁵ 以内的答案可以被接受。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[3.00000,14.50000,11.00000]
# 解释：第 0 层的平均值为 3,第 1 层的平均值为 14.5,第 2 层的平均值为 11 。
# 因此返回 [3, 14.5, 11] 。
#  
# 
#  示例 2: 
# 
#  
# 
#  
# 输入：root = [3,9,20,15,7]
# 输出：[3.00000,14.50000,11.00000]
#  
# 
#  
# 
#  提示： 
# 
#  
#  
# 
#  
#  树中节点数量在 [1, 10⁴] 范围内 
#  -2³¹ <= Node.val <= 2³¹ - 1 
#  
# 
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 569 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

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
                if node.left:  queue.append(node.left)
                if node.right: queue.append(node.right)

            res.append(sum(current_level)/len(current_level))

        return res
# leetcode submit region end(Prohibit modification and deletion)
