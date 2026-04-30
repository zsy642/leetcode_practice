class MyQueue:
    def __init__(self):
        self.old=[]
        self.new=[]
    def push(self, x: int) -> None:
        self.old.append(x)

    def pop(self) -> int:
        if not self.new:
            self.new=self.old[::-1]
            self.old=[]
        return self.new.pop()

    def peek(self) -> int:
        if not self.new:
            self.new=self.old[::-1]
            self.old=[]
        return self.new[-1]
    def empty(self) -> bool:
        return (len(self.old)+len(self.new))==0