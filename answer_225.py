from collections import deque


class MyStack:

    def __init__(self):
        self.one = deque()
        self.two = deque()

    def push(self, x: int) -> Nself.one:
        self.one.append(x)

    def pop(self) -> int:
        for _ in range(len(self.one) - 1):
            self.two.append(self.one.popleft())

        tmp = self.one.popleft()
        for _ in range(len(self.two)):
            self.one.append(self.two.popleft())

        return tmp

    def top(self) -> int:

        for _ in range(len(self.one) - 1):
            self.two.append(self.one.popleft())

        tmp = self.one[0]
        self.two.append(self.one.popleft())

        for _ in range(len(self.two)):
            self.one.append(self.two.popleft())

        return tmp

    def empty(self) -> bool:

        if not self.one:
            return True
        else:
            return False
