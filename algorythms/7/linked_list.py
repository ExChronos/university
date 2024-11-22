class linkedListNode:
    def __init__(self, value, next):
        self.value=value
        self.next=next

class linkedList:
    head=None

    def add(self, value):
        self.head=linkedListNode(value, self.head)
    
    def addToEnd(self, value):
        current=self.head

        while current.next is not None:
            if current.next is None:
                current=linkedListNode(value, None)

    def deleteOne(self):
        if self.head is None:
            return None
        
        value=self.head.value
        self.head=self.head.next

        return value


    def deleteItem(self, value):
        current=self.head

        if current is None:
            return None

        elif current.next is None:
            return self.deleteOne()
        
        else:
            while current.next is not None and current.value is not value:
                current=current.next
                current.value=value
            
            nextValue=current.next.value
            current.next=current.next.next
        
            return nextValue
        