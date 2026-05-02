# 给定一个字符串 s 和一个整数 k，从字符串开头算起，每计数至 2k 个字符，就反转这 2k 字符中的前 k 个字符，再重新计数。 
# 
#  
#  如果剩余字符少于 k 个，则将剩余字符全部反转。 
#  如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "abcdefg", k = 2
# 输出："bacdfeg"
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "abcd", k = 2
# 输出："bacd"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 10⁴ 
#  s 仅由小写英文组成 
#  1 <= k <= 10⁴ 
#  
# 
#  Related Topics 双指针 字符串 👍 719 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 定义操作符映射，逻辑更清晰
        operators = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            # 关键：使用 int(a / b) 实现向零截断
            '/': lambda a, b: int(a / b)
        }

        stack = []
        for token in tokens:
            if token in operators:
                # 注意：后弹出来的是左操作数
                num2 = stack.pop()
                num1 = stack.pop()
                # 执行运算并把结果（int）直接压回栈
                stack.append(operators[token](num1, num2))
            else:
                # 只有入栈时转换一次 int
                stack.append(int(token))

        return stack[0]
# leetcode submit region end(Prohibit modification and deletion)
