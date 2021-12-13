from code_challenge32 import __version__
from code_challenge32.tree_intersection import tree_intersection
from code_challenge32.trees import BinaryTree,Node
import pytest


def test_version():
    assert __version__ == '0.1.0'


def test_tree_intersection(tree_i):
    actual = tree_i
    expected=['A', 'B']
    assert actual == expected



@pytest.fixture()
def tree_i():
    tree1=BinaryTree()
    tree1.root=Node("A")
    tree1.root.left=Node("B")
    tree1.root.right=Node("C")
    tree1.root.left.left=Node("D")
    tree1.root.left.right=Node("E")
    tree1.root.right.left=Node("F")

    tree2=BinaryTree()
    tree2.root=Node("A")
    tree2.root.left=Node("B")
    tree2.root.right=Node("k")
    tree2.root.left.left=Node("r")
    tree2.root.left.right=Node("x")
    tree2.root.right.left=Node("m")

    return tree_intersection(tree1,tree2)
