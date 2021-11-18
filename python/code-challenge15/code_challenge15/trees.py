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
        self.output.append(root.value)
        if root.left != None:
            self.pre_order(root.left)
        if root.right != None:
            self.pre_order(root.right)
        
        return self.output


    def in_order(self,root):

        if root.left is not None:
            self.in_order(root.left)
        
        self.output.append(root.value)

        if root.right is not None:
            self.in_order(root.right)
        
        return self.output
        

    def post_order(self,root):
        if root.left is not None:
            self.post_order(root.left)
        
        if root.right is not None:
            self.post_order(root.right)
        
        self.output.append(root.value)
        
        return self.output


class BinarySearchTree(BinaryTree):

    def add(self,value):
        pass

    def contain(self,value):
        return self.output
    


if __name__ == "__main__":
    tree=BinaryTree()
    tree.root=Node("A")
    tree.root.left=Node("B")
    tree.root.right=Node("C")
    tree.root.left.left=Node("D")
    tree.root.left.right=Node("E")
    tree.root.right.left=Node("F")
    print("pre :",tree.pre_order(tree.root))
    print(BinarySearchTree().contain("B"))
    # print("in :",tree.in_order(tree.root))
    # print("post:",tree.post_order(tree.root))