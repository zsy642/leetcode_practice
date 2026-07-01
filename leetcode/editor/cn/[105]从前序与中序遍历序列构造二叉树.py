# 给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并
# 返回其根节点。 
# 
#  
# 
#  示例 1: 
#  
#  
# 输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# 输出: [3,9,20,null,null,15,7]
#  
# 
#  示例 2: 
# 
#  
# 输入: preorder = [-1], inorder = [-1]
# 输出: [-1]
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= preorder.length <= 3000 
#  inorder.length == preorder.length 
#  -3000 <= preorder[i], inorder[i] <= 3000 
#  preorder 和 inorder 均 无重复 元素 
#  inorder 均出现在 preorder 
#  preorder 保证 为二叉树的前序遍历序列 
#  inorder 保证 为二叉树的中序遍历序列 
#  
# 
#  Related Topics 树 数组 哈希表 分治 二叉树 👍 2763 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 1. 用哈希表给中序遍历建一个“快速索引字典”，实现 O(1) 查找
        inorder_map = {val: i for i, val in enumerate(inorder)}

        # 2. 闭包函数，只传四个指针，死死咬住当前子树在原数组里的范围
        def myBuildTree(pre_left, pre_right, in_left, in_right):
            # 边界条件：指针错位了，说明没有节点了
            if pre_left > pre_right:
                return None

            # 前序遍历的第一个元素是根节点
            root_val = preorder[pre_left]
            root = TreeNode(root_val)

            # O(1) 查出根节点在中序遍历中的位置
            in_root_index = inorder_map[root_val]

            # 算出左子树的节点个数，这是原数组里的“黄金跨度”
            left_subtree_size = in_root_index - in_left

            # 递归分配任务，纯指针算术，零内存拷贝：1qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqa                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
            root.left = myBuildTree(
                pre_left + 1, pre_left + left_subtree_size,
                in_left, in_root_index - 1
            )
            root.right = myBuildTree(
                pre_left + left_subtree_size + 1, pre_right,
                in_root_index + 1, in_right
            )

            return root

        n = len(preorder)
        return myBuildTree(0, n - 1, 0, n - 1)
# leetcode submit region end(Prohibit modification and deletion)
