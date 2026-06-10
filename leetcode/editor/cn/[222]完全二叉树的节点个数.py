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
        # finddepth形参节点,返回值深度(算自己也算叶子)和底层叶子数
        def finddepth(root):
            #退出条件如果是叶子返回1,0,如果是一个叶子返回2,1
            if not root.left and not root.right:
                return 1,0
            if not root.left or not root.right:
                return 2,1
            #每次先左调用一次,判断没有叶子再进行右边调用,否则直接返回高度和叶子数
            deepl,numl=finddepth(root.left)
            if not numl:
                # 如果没有叶子记得调用右边,最后返回左边的深度和右边叶子树+左边的叶子,代入的时候不减一  ps:完美二叉树叶子节点数 n₀：刚好等于 \(2^{h-1}\)
                deepr, numr = finddepth(root.right)
                if deepr==deepl and not numr:
                    return deepl + 1, 0
                else:
                    return deepl+1,2**(deepl-1)+numr
            else:
                return deepl+1,numl

        #调用finddepth(root),最后得到结果计算,代入的时候深度要减一+叶子数或者不减一如果叶子是0的话   ps:完美二叉树总节点数 n 与高度 h 的关系：\(n = 2^h - 1\)
        deep,num=finddepth(root)
        #print(deep,num)
        if not num:
            return 2**deep-1
        else:
            return 2**(deep-1)-1+num

        
# leetcode submit region end(Prohibit modification and deletion)
