class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
class LinkedList:
 
    def __init__(self):
        self.head = None
 
    def add(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
 
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
 
def is_cycling(ll):
    curr = ll.head
    old_nodes = []
    while (curr):
        if (curr in old_nodes):
            return True
        old_nodes.append(curr)
        curr = curr.next
    return False

if __name__ == "__main__":
    lil = LinkedList()
    lil.add(1)
    lil.add(2)
    lil.add(3)
    lil.add(4)
    lil.head.next.next.next.next = lil.head.next

    print(is_cycling(lil))
