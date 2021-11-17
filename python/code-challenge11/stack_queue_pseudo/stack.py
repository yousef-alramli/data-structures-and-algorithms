class Node:
    def __init__ (self , value):
        self.next = None
        self.value = value
    
class Stack:
    def __init__(self):
        self.top = None

    def push(self,value):
        node = Node(value)
        if self.top == None:
            self.top = node
        else:
            node.next = self.top
            self.top = node
        
         
    def pop(self):
        if self.top == None:
            raise Exception("sorry no elements")
        temp = self.top
        self.top = self.top.next
        temp.next = None
        return temp.value
    
    def peek(self):
        if self.top == None:
            raise Exception("sorry no elements")
        return self.top.value
    def is_empty(self):
        return self.top == None


        