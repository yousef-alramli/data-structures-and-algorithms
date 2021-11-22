class Node:
    def __init__(self,value):
        self.right = None
        self.left = None
        self.value = value

class BinaryTree:
    def __init__(self):
        self.root = None
        self.output = []

    def pre_order(self, root):
        if root == None:
            return self.output

        self.output.append(root.value)
        if root.left != None:
            self.pre_order(root.left)
        if root.right != None:
            self.pre_order(root.right)
        
        return self.output


    def in_order(self,root):
        if root == None:
            return self.output

        if root.left is not None:
            self.in_order(root.left)
        
        self.output.append(root.value)

        if root.right is not None:
            self.in_order(root.right)
        
        return self.output
        

    def post_order(self,root):
        if root == None:
            return self.output
        
        if root.left is not None:
            self.post_order(root.left)
        
        if root.right is not None:
            self.post_order(root.right)
        
        self.output.append(root.value)
        
        return self.output


class BinarySearchTree(BinaryTree):
    def __init__(self):
        super().__init__()

    def add(self,value):
        node = Node(value)
        if self.root == None:
            self.root = node
        
        else:
            temp = self.root
            if temp.value < node.value:
                while temp.right != None:
                    temp = temp.right
                temp.right = node

            elif temp.value > node.value:
                while temp.left != None:
                    temp = temp.left
                temp.left = node
            

    def contain(self,value):
        
        temp = self.root
        if temp == None:
            return False

        if temp.value == value:
            return True
        
        if temp.value < value:
            while temp != None and temp.value < value:
                temp = temp.right
                if temp != None and temp.value == value:
                    return True
            return False
        
        if temp.value > value: 
            while temp != None and temp.value > value:
                temp = temp.left
                if temp != None and temp.value == value:
                    return True

            return False
    


if __name__ == "__main__":
    tree=BinaryTree()
    tree.root=Node("A")
    tree.root.left=Node("B")
    tree.root.right=Node("C")
    tree.root.left.left=Node("D")
    tree.root.left.right=Node("E")
    tree.root.right.left=Node("F")
    search_tree = BinarySearchTree()
    search_tree.add(15)
    search_tree.add(14)
    search_tree.add(4)
    search_tree.add(23)



    # print(search_tree.root.left.value)
    print(search_tree.contain(5) == False)

