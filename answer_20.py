class Solution:
    def isValid(self, s: str) -> bool:
        # 用字典管理匹配规则，想加多少种括号加多少种
        mapping = {'(': ')', '[': ']', '{': '}'}
        stack = []

        for char in s:
            if char in mapping:
                # 遇到左括号，把对应的右括号压栈
                stack.append(mapping[char])
            else:
                # 遇到右括号，进行验证
                if not stack or char != stack[-1]:
                    return False
                stack.pop()

        return not stack  # 等同于 if stack: return False else: return True