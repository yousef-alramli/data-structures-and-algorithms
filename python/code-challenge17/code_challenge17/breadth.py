from collections import deque

def breadth_first(tree):
    breadth = deque()
    breadth.append(tree.root)
    output = []
    while breadth:
        front = breadth.popleft()
        output.append(front.value) 
    
        if front.left is not None:
            breadth.append(front.left)
        
        if front.right is not None:
            breadth.append(front.right)
    
    return output
    

