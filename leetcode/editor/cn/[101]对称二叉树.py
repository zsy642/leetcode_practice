# 给你一个二叉树的根节点 root ， 检查它是否轴对称。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [1,2,2,3,4,4,3]
# 输出：true
#  
# 
#  示例 2： 
#  
#  
# 输入：root = [1,2,2,null,3,null,3]
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数目在范围 [1, 1000] 内 
#  -100 <= Node.val <= 100 
#  
# 
#  
# 
#  进阶：你可以运用递归和迭代两种方法解决这个问题吗？ 
# 
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 3152 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        stack1=[root.left]
        stack2=[root.right]

        while stack1 and stack2:
            tmp1=stack1[-1]
            tmp2=stack2[-1]
            if  not tmp1 and not tmp2:
                pass
            elif (not tmp1 and tmp2) or (not tmp2 and tmp1) or tmp1.val != tmp2.val:
                return False


            if tmp1 and (tmp1.left or tmp1.right):
                stack1.append(tmp1.left)
                stack2.append(tmp2.right)
            else :
                if not stack1 or not stack2:
                    break
                stack1.pop()
                stack2.pop()
                if not stack1 or not stack2:
                    break
                tmp1 = stack1.pop()
                tmp2 = stack2.pop()
                stack1.append(tmp1.right)


                stack2.append(tmp2.left)

        if stack1 or stack2:
            return False
        return True




# leetcode submit region end(Prohibit modification and deletion)
