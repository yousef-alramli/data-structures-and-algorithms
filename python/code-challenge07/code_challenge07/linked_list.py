class Node :
    def __init__ (self,value):
        self.value = value
        self.next = None

class Linked_List:
    def __init__ (self):
        self.head = None
    
    def append_to_last(self,value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node


    def kthFromEnd(self,k):
        kth = []
        current = self.head
        while (current):
            kth.append(current.value)
            current = current.next
        kth = kth[::-1]
        if k >= len(kth) or k < 0:
            return "Exception"
        else:
            return kth[k]

    def __str__(self):
        output = ""
        current = self.head
        while (current):
            output += f"{current.value} -> "
            current = current.next
        output += "Null"
        
        return output
        

if __name__=="__main__":
    lil = Linked_List()
    lil.append_to_last("baba")
    lil.append_to_last("sd")
    lil.append_to_last(5)
    lil.append_to_last("sdas")
    lil.append_to_last("val34322ue")
    lil.append_to_last(42)
    x = lil.__str__().split(" -> ")
    x.remove('Null')
    print(lil.kthFromEnd(0))