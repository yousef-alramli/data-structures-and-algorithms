class Node:
    def __init__(self,value):
        self.next = None
        self.value = value




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
        print(self.rear.value)
        
    
    def dequeue(self, pref=None):

        if self.rear == None:
            raise Exception("Sorry, this queue is empty")
        temp = self.front
        self.front = self.front.next
        temp.next = None
        return temp.value




class Dog():
    def __init__(self, name):
        self.type = "Dog"
        Queue().enqueue(name)


class Cat():
    def __init__(self):
        self.type = "Cat"
        Queue().enqueue(name)

        


    


