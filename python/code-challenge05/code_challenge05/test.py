from trees import BinaryTree
from trees import Node as treenode


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

def delete_node(ll,n):
    curr = ll.head
    if curr.value == n:
        ll.head = curr.next
    # print("kofk;fsdds")
    while curr.next:
        # print(curr.next.value)
        if curr.next.value == n:
            print("in if ")
            temp = curr
            temp = curr.next
            curr.next = temp.next
            temp = None

        if curr.next:
            curr = curr.next

    



# def reverse(ll):
#     first = ll.head
#     curr = ll.head
#     prev = None

#     while curr:
#         nex = curr.next
#         curr.next = prev
#         prev = curr
#         curr = nex
#     ll.head = prev
#     second = ll.head
#     while first.next:
#         if first.value != second.value:
#             print(False)
#         print(first , second)
#         first = first.next
#         second = second.next 
        


# def reverse(ll):
#     current = ll.head
#     output = ''
#     while current.next != None:
#         output = f"{current.value} -> " + output
#         current = current.next
#     output += "NONE"
#     return output

def rotate(ll,k):
    curr = ll.head
    count = 1


    while count < k and curr:
        curr = curr.next
        count += 1

    if curr == None:
        return

    kthNode = curr

    while curr.next:
        curr=curr.next
    curr.next = ll.head
    ll.head = kthNode.next
    kthNode.next = None
    


def middle(ll):
    first = ll.head
    
    count = 0
    while first:
        count +=1
        first = first.next
    
    count = count//2
    count2 = 0
    second = ll.head
    # print(second.next.value , count)
    while count2 < count:
        count2 +=1
        second = second.next
    ll.head = second



# def printPaths(root):

#     path = []
#     getting_paths(root, path, 0)
 
# # Helper function to print path from root
# # to leaf in binary tree
# def getting_paths(root, path, pathLen):
     

#     if root == None:
#         return "empty list"
 
#     # add current root's value into
#     # path_ar list
     
#     # if length of list is gre
#     if len(path) > pathLen:
#         path[pathLen] = root.value
#     else:
#         path.append(root.value)
 
#     # increment pathLen by 1
#     pathLen = pathLen + 1
 
#     if root.left is None and root.right is None:
         
#         # leaf node then print the list
#         printArray(path, pathLen)
#     else:
#         # try for left and right subtree
#         getting_paths(root.left, path, pathLen)
#         getting_paths(root.right, path, pathLen)


# # Helper function to print list in which
# # root-to-leaf path is stored
# def printArray(ints, len):
#     for i in ints[0 : len]:
#         print(i,"->",end="")
#     print()

def sum_left(root,summing = 0):

    
    if root.left:

        summing += root.left.value
        summing =sum_left(root.left, summing)



    if root.right:
        summing =sum_left(root.right, summing)

    return summing


if __name__ == "__main__":
    tree = BinaryTree()
    # tree.root=treenode("A")
    # tree.root.left=treenode("B")
    # tree.root.left.left=treenode("D")
    # tree.root.left.right=treenode("E")
    # tree.root.right=treenode("C")
    # tree.root.right.left=treenode("F")
    
# [1,2,3,4,5]
    tree.root=treenode(1)
    tree.root.left=treenode(2)
    tree.root.left.left=treenode(4)
    tree.root.left.right=treenode(5)
    tree.root.right=treenode(3)
    # tree.root.right.left=treenode(6)
    print(sum_left(tree.root))
    # lil = LinkedList()
    # lil.add(1)
    # lil.add(1)
    # lil.add(6)
    # lil.add(4)
    # lil.add(4)
    # lil.add(6)
    # lil.add(8)
    # lil.add(8)
    # lil.odd_even()
    # lil.rmv_dublicate()
    # print(lil.__str__())
    # rotate(lil,2)
    # print(lil.__str__())
    # lil.remove_nth(7)

