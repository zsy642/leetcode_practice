def removeDuplicates(s: str) -> str:
    stack = []
    for i in s:
        if stack == [] or i != stack[-1]:
            stack.append(i)
        else:
            stack.pop()
    stack = ''.join(stack)
    return stack