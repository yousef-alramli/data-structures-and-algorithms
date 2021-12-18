
# https://leetcode.com/problems/binary-tree-paths/

# Time : O(N*N) not sure

# Space: O(2n)

# 257. Binary Tree Paths
# Given the root of a binary tree, return all root-to-leaf paths in any order.
# A leaf is a node with no children.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binaryTreePaths(root):
    def dfs(root):
        if not root:
            return "empty list"
        if not root.left and not root.right:
            tmp.append(str(root.val))
            res.append("->".join(tmp))
            tmp.pop()
            return
        tmp.append(str(root.val))
        dfs(root.left)
        dfs(root.right)
        tmp.pop()
    tmp = []
    res = []
    dfs(root)
    return res

if __name__ == "__main__":

    # tree1 = TreeNode(4)

    # tree1.left = TreeNode(2)
    # tree1.right = TreeNode(7)

    # tree1.left.left = TreeNode(1)
    # tree1.left.right = TreeNode(3)

    # tree1.right.left = TreeNode(6)
    # tree1.right.right = TreeNode(9)

    tree1 = TreeNode(1)

    tree1.left = TreeNode(2)
    tree1.right = TreeNode(3)

    tree1.left.right = TreeNode(5)

    print(binaryTreePaths(tree1))