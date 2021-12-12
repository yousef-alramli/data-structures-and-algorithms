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
        
    def append_before(self,value,new_value):
        values_list =[]
        node = Node(new_value)
        current = self.head
        while current.next is not None:
            values_list.append(current.next.value)
            values_list.append(current.value)
            if current.next.value == value:
                break 
            current = current.next
        if value in values_list:
            node.next = current.next
            current.next = node

    def append_after(self,value,new_value):
        values_list =[]
        node = Node(new_value)
        current = self.head
        while current.next is not None:
            values_list.append(current.next.value)
            values_list.append(current.value)
            if current.value == value:
                break  
            current = current.next
        if value in values_list:
            node.next = current.next
            current.next = node

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
    lil.append_before(5,5959595)
    lil.append_after("sd","dsdssddssd")
    print(lil.__str__())