class MyQueue:

    def __init__(self):
        self.old=[]
        self.new=[]
    def push(self, x: int) -> None:
        self.old.append(x)

    def pop(self) -> int:
        self.new=self.old[::-1]
        tmp=self.new.pop()
        self.old=self.new[::-1]
        self.new=[]
        return tmp

    def peek(self) -> int:
        self.new=self.old[::-1]
        tmp=self.new[-1]
        self.new=[]
        return tmp
    def empty(self) -> bool:
        return len(self.old)!=0

x=MyQueue()
x.push(2)
x.push(3)
x.pop()
x.pop()
print(x.peek())