# 给你二叉树的根节点 root ，返回它节点值的 前序 遍历。 
# 
#  
# 
#  示例 1： 
# 
#  
#  输入：root = [1,null,2,3] 
#  
# 
#  输出：[1,2,3] 
# 
#  解释： 
# 
#  
# 
#  示例 2： 
# 
#  
#  输入：root = [1,2,3,4,5,null,8,null,null,6,7,9] 
#  
# 
#  输出：[1,2,4,5,6,7,3,8,9] 
# 
#  解释： 
# 
#  
# 
#  示例 3： 
# 
#  
#  输入：root = [] 
#  
# 
#  输出：[] 
# 
#  示例 4： 
# 
#  
#  输入：root = [1] 
#  
# 
#  输出：[1] 
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数目在范围 [0, 100] 内 
#  -100 <= Node.val <= 100 
#  
# 
#  
# 
#  进阶：递归算法很简单，你可以通过迭代算法完成吗？ 
# 
#  Related Topics 栈 树 深度优先搜索 二叉树 👍 1403 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def universalTraversal(root, order_type="in"):
        if not root:
            return []

        res = []
        # 栈中元素格式为: (node, visited)
        # visited 为 False 表示第一次遇到，为 True 表示可以访问了
        stack = [(root, False)]

        while stack:
            node, visited = stack.pop()

            if not node:
                continue

            # 情况一：如果该节点已经是第二次相遇，直接收集结果
            if visited:
                res.append(node.val)

            # 情况二：第一次遇到该节点，将其和子节点按“逆序”压栈
            else:
                if order_type == "pre":
                    # 前序期望输出：根 -> 左 -> 右
                    # 栈是 LIFO，所以入栈逆序：右 -> 左 -> 根
                    stack.append((node.right, False))
                    stack.append((node.left, False))
                    stack.append((node, True))  # 标记为 True，下次弹出直接打印

                elif order_type == "in":
                    # 中序期望输出：左 -> 根 -> 右
                    # 栈是 LIFO，所以入栈逆序：右 -> 根 -> 左
                    stack.append((node.right, False))
                    stack.append((node, True))  # 标记为 True
                    stack.append((node.left, False))

                elif order_type == "post":
                    # 后序期望输出：左 -> 右 -> 根
                    # 栈是 LIFO，所以入栈逆序：根 -> 右 -> 左
                    stack.append((node, True))  # 标记为 True
                    stack.append((node.right, False))
                    stack.append((node.left, False))

        return res

# leetcode submit region end(Prohibit modification and deletion)
