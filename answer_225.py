from collections import deque

class MyStack:
    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        # 只需原地转圈 n-1 次
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())
        return self.queue.popleft()

    def top(self) -> int:
        res = self.pop()
        self.queue.append(res)
        return res

    def empty(self) -> bool:
        return not self.queue
