from stack import Stack , Node


class PseudoQueue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self , value):
        self.s1.push(value)
        
           
    def dequeue(self):
        while not self.s1.is_empty():
            self.s2.push(self.s1.pop())
        



        return self.s2.pop()
    

if __name__ == "__main__":
    queue = PseudoQueue()
    queue.enqueue("value")
    queue.enqueue("hello")
    queue.enqueue("1234")
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    


        


