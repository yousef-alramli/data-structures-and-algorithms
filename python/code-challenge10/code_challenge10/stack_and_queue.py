class Node :
    def __init__(self,value):
        self.value = value
        self.next = None


class Stack :
    def __init__ (self):
        self.top = None
    
    def push(self,value):
        node = Node(value)
        if self.top :
            node.next = self.top
        
        self.top = node

    def pop(self):
        if self.top == None:
            raise Exception("Sorry, this stack is empty")
        temp = self.top
        self.top=self.top.next
        temp.next = None 
        return temp.value
    
    def peek(self):
        if self.top == None:
            raise Exception("Sorry, this stack is empty")
        return self.top.value
    
    def is_empty(self):
        return self.top == None



class Queue:
    def __init__(self):
        self.rear = None
        self.front = None

    
    def enqueue(self,value):
        node = Node(value)
        if self.rear == None:
            self.rear = node
            self.front = node
        else:
            self.rear.next = node
            self.rear = node
    
    def dequeue(self):
        if self.rear == None:
            raise Exception("Sorry, this queue is empty")
        temp = self.front
        self.front = self.front.next
        temp.next = None
        return temp.value

    def peek(self):
        if self.rear == None:
            raise Exception("Sorry, this queue is empty")
        return self.front

    def is_empty(self):
        return self.front == None

    







