# 给定一个 N 叉树，返回其节点值的层序遍历。（即从左到右，逐层遍历）。 
# 
#  树的序列化输入是用层序遍历，每组子节点都由 null 值分隔（参见示例）。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：root = [1,null,3,2,4,null,5,6]
# 输出：[[1],[3,2,4],[5,6]]
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,
# null,13,null,null,14]
# 输出：[[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  树的高度不会超过 1000 
#  树的节点总数在 [0, 10⁴] 之间 
#  
# 
#  Related Topics 树 广度优先搜索 👍 523 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
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
                for i in node.children:
                    queue.append(i)


            res.append(current_level)

        return res
# leetcode submit region end(Prohibit modification and deletion)
