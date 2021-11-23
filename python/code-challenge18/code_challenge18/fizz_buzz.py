from code_challenge18.queue_and_node import Node , Queue

class KAryTrees:
    def __init__(self):
        self.front = None
        self.children = []

    def breadthFirst(root):
        breadth = Queue()
        breadth.enqueue(root)
        output = []

        while breadth.peek():
            self.front = breadth.dequeue()
            output.append(self.front)

            for child in self.front.children:
                breadth.enqueue(child)







def fizz_buzz_tree(k_tree):
    pass
