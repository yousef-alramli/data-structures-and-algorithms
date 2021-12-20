
# https://leetcode.com/problems/minimum-absolute-difference-in-bst/

# O(n) time
# O(1) space

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def getMinimumDifference(root):
    global res, prev
    res = float('inf')
    prev = -float('inf')
    
    def inOrder(root):
        global res, prev
        if root.left:
            inOrder(root.left)
        res = min(root.val - prev, res)
        prev = root.val
        if root.right:
            inOrder(root.right)
            
    inOrder(root)
    return res


if __name__ == "__main__":

    tree1 = TreeNode(4)

    tree1.left = TreeNode(90)
    tree1.right = TreeNode(6)

    tree1.left.left = TreeNode(1)
    tree1.left.right = TreeNode(3)

    # tree1.right.left = TreeNode(2)
    # tree1.right.right = TreeNode(9)

    tree2 = TreeNode(1)

    tree2.left = TreeNode(0)
    tree2.right = TreeNode(48)

    # tree2.left.left = TreeNode(1)
    # tree2.left.right = TreeNode(3)

    tree2.right.left = TreeNode(12)
    tree2.right.right = TreeNode(49)

    print(getMinimumDifference(tree1))
    # print(getMinimumDifference(tree2))