class Node :
    def __init__(self,value):
        self.value = value
        self.next = None


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

    







