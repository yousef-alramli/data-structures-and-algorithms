
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Linked_In_List:
    def __init__(self):
        self.head = None
    
    def appending (self,value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            current_value = self.head
            while current_value.next != None:
                current_value = current_value.next
            current_value.next = node
    
    def __str__(self):
        output = ""
        current_value = self.head
        # print(current_value)
        while (current_value):
            output += f"{current_value.value} -> "
            current_value = current_value.next
        output += "Null"
        
        return output

if __name__=="__main__":
    lil = Linked_In_List()
    lil.appending("baba")
    lil.appending("sd")
    lil.appending(5)
    lil.appending("sdas")
    lil.appending("val34322ue")
    lil.appending(42)
    print(lil.head.value)


        


