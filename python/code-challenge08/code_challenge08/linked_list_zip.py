class Node :
    def __init__ (self,value):
        self.value = value
        self.next = None

class Linked_List1:
    def __init__ (self):
        self.head = None
    
    def append(self,value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node

    def __str__(self):
        output = ""
        current = self.head
        while (current):
            output += f"{current.value} -> "
            current = current.next
        output += "Null"
        
        return output

class Linked_List2:
    def __init__ (self):
        self.head = None
    
    def append(self,value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node

    def __str__(self):
        output = ""
        current = self.head
        while (current):
            output += f"{current.value} -> "
            current = current.next
        output += "Null"
        
        return output

def zipLists(list1, list2):
    output = ''
    first = list1.__str__().split(" -> ")
    first.remove('Null')
    second = list2.__str__().split(" -> ")
    second.remove('Null')

    for i in range(len(first)):
        output += f"{second[i]} -> "
        output += f"{first[i]} -> "
    output += "Null"
    return output




if __name__=="__main__":
    lil1 = Linked_List1()
    lil2 = Linked_List2()

    lil1.append("baba")
    lil1.append("sd")
    lil1.append(5)

    lil2.append("sdas")
    lil2.append("val34322ue")
    lil2.append(42)

    # print(lil1.__str__())
    # print(lil2.__str__())
    print("==================")
    print(zipLists(lil1, lil2))



