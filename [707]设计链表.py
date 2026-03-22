class MyLinkedList:
    class LinkedList:
        def __init__(self,val=0,next=None):
            self.val=val
            self.next=next

    def __init__(self):
        self.size=0
        self.virus=self.LinkedList(10086)

    def get(self, index: int) -> int:
        if index<0 or index>=self.size:
            return -1
        tmp=self.virus
        for _ in range(index+1):
            tmp=tmp.next
        return tmp.val

    def addAtHead(self, val: int) -> None:
        head=self.LinkedList(val)
        head.next=self.virus.next
        self.virus.next=head
        self.size+=1

    def addAtTail(self, val: int) -> None:
        tail=self.LinkedList(val)
        tmp=self.virus
        while tmp.next:
            tmp=tmp.next
        tmp.next=tail
        self.size+=1

    def addAtIndex(self, index: int, val: int) -> None:
        if index<0 or index>self.size:
            return None
        elif index==self.size:
            self.addAtTail(val)
        else:
            link=self.LinkedList(val)
            tmp=self.virus
            for _ in range(index):
                tmp=tmp.next
            link.next=tmp.next
            tmp.next=link
            self.size+=1


    def deleteAtIndex(self, index: int) -> None:
        if index<0 or index>=self.size:
            return None
        else:
            tmp=self.virus
            for _ in range(index):
                tmp=tmp.next
            tmp.next=tmp.next.next
            self.size-=1