class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add(self,value):
        node = Node(value)
        if self.head == None:
            self.head = node

        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node
    
    def remove_nth(self,n):
        current = self.head
        if current != None:
            if n == 1:
                self.head = current.next
                return
            num = 1

            while num != n - 1:
                num += 1
                current = current.next
            prev = current
            current = current.next
            prev.next = current.next
            current = None


    def rmv_dublicate(self):
        prev = self.head
        current = prev.next
        while current:
            
            if prev.value == current.value:
                prev.next = current.next
            prev = current
            current=current.next
            
    
    def odd_even(self):
        prev = None
        end = self.head
        current = self.head

        while end.next != None:
            end = end.next
        
        new_end = end

        while current.value%2 == 1 and current != new_end:
            new_end.next = current
            current = current.next
            new_end.next.next = None
            new_end = new_end.next
            
        if current.value % 2 == 0:
            self.head = current

            while current != new_end:
			
                if current.value % 2 == 0:
                    prev = current
                    current = current.next
                else:
                    prev.next = current.next
                    current.next = None
                    new_end.next = current
                    new_end = current
                    current = prev.next
        else:
            prev = current
        
        if new_end != end and end.value % 2 == 1:
            prev.next = end.next
            end.next = None
            new_end.next = end



    def __str__(self):
        output = ''
        current = self.head
        while current != None:
            output += f"{current.value} -> "
            current = current.next
        output += "NONE"
        return output

def reverse(ll):
    current = ll.head
    output = ''
    while current.next != None:
        output = f"{current.value} -> " + output
        current = current.next
    output += "NONE"
    return output



if __name__ == "__main__":
    lil = LinkedList()
    lil.add(1)
    lil.add(1)

    lil.add(3)
    lil.add(4)
    lil.add(4)
    lil.add(4)
    lil.add(6)
    lil.add(8)
    lil.add(8)
    lil.odd_even()
    # lil.rmv_dublicate()
    # lil.remove_nth(7)
    print(lil.__str__())
