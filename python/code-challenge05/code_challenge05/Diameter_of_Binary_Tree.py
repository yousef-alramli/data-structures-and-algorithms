
# https://leetcode.com/problems/diameter-of-binary-tree/

# O(n) time
# O(1) space

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameterOfBinaryTree(root):
    def dfs(root):
        if not root:
            return 0, 0
        l = dfs(root.left)
        r = dfs(root.right)
        here = max(l[0], r[0])+1
        return here, max(l[1], r[1], l[0]+r[0]+1)
    res = dfs(root)[1]
    return res-1 if res > 0 else 0

def testing(root):
    if not root.right and not root.left:
        return 0
    
    def rex(root,count = 1):
        if not root:
            return 0
        if root.left:
            count += 1
            count = rex(root.left,count)
            # if root.left.right:
            #     count -=1
        # l = rex(root.left,count)+1
        # r = rex(root.right,count)+1
        # count =l+r
        if root.right:
            count += 1
            count = rex(root.right,count)
        if root.left and root.right:
            count -=1
            return count

            # if root.right.left:
        return count

        
    
    return rex(root)
    

    

if __name__ == "__main__":

    tree1 = TreeNode(1)

    # tree1.left = TreeNode(2)
    # tree1.right = TreeNode(3)

    # tree1.left.left = TreeNode(4)
    # tree1.left.right = TreeNode(5)
    # tree1.left.left.left = TreeNode(4)


    # tree1.right.left = TreeNode(15)
    # tree1.right.right = TreeNode(7)
    # tree1.right.right.left = TreeNode(8)
    # tree1.right.right.right = TreeNode(9)


    print(diameterOfBinaryTree(tree1))
    print(testing(tree1))

