class Stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)
    
    def isEmpty(self):
        return self.items == []
    
    def pop(self):
        if self.isEmpty():
            raise Empty("Stack is empty.")
        return self.items.pop()
    
    def peek(self):
            '''if self.isEmpty():
                raise Empty("Stack is empty.")'''
            return self.items[len(self.items)-1]
    
    def size(self):
        return self.items.len()
    
    def disp(self):
        item=self.items
        while item:
            return item
        
ss=Stack()
ss.push(5)
ss.push(4)
ss.push(3)
print(ss.disp())
#print(ss.isEmpty())
'''print(ss.peek())
ss.pop()
ss.pop()
ss.pop()
print(ss.isEmpty())'''