class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self,value):
        node = Node(value)
        if self.front == None:
            self.front = node 
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        return self.front.value
        
    def dequeue(self):
        if self.front == None:
            raise Exception("sorry no data here")
        temp = self.front
        self.front = self.front.next
        temp.next = None    
    
    def all_nodes(self):
        output = []
        while (self.front):
            output.append(self.front.value)
            self.front = self.front.next
        return output


a = [1,2,3,4,5,6,7]
b = []

print(a[::-1])

if __name__ == "__main__":
    pass