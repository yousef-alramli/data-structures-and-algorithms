
# https://leetcode.com/problems/sum-of-left-leaves/

# O(n) time
# O(1) space

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sumOfLeftLeaves(root):
    global ans
    ans = 0

    def dfs(r, d):
        global ans
        if not r:
            return
        if not r.left and not r.right and d:
            ans += r.val
        dfs(r.left, 1)
        dfs(r.right, 0)
    dfs(root, 0)
    return ans


if __name__ == "__main__":

    tree1 = TreeNode(3)

    tree1.left = TreeNode(9)
    tree1.right = TreeNode(20)

    tree1.left.left = TreeNode(9)
    # tree1.left.right = TreeNode(5)

    tree1.right.left = TreeNode(15)
    tree1.right.right = TreeNode(7)

    print(sumOfLeftLeaves(tree1))
