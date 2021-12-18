
# https://leetcode.com/problems/find-mode-in-binary-search-tree/

# O(2n) time
# O(n) space

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findMode(root):
    def h(node, l):
        if node is None:
            return l
        if(node.val in l):
            l[node.val] += 1
        else:
            l[node.val] = 1
        if(node.left is not None):
            h(node.left, l)
        if(node.right is not None):
            h(node.right, l)
        return l
    l = {}
    h(root, l)
    m = max(l.values())

    result = ""
    for i, v in l.items():
        if(v == m):
            result = i
    return result

    # return (i for i, v in l.items() if(v == m))


if __name__ == "__main__":

    tree1 = TreeNode(1)

    tree1.left = TreeNode(9)
    tree1.right = TreeNode(2)

    tree1.left.left = TreeNode(9)

    tree1.right.left = TreeNode(2)
    tree1.right.right = TreeNode(9)

    result = findMode(tree1)
    print(result)
