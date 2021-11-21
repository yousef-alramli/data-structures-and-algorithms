from code_challenge16 import __version__
from code_challenge16.binary_tree import Node,BinaryTree
import pytest

def test_version():
    assert __version__ == '0.1.0'

def test_max_num(tree):
    actual = tree.maximum_value()
    expected = 200
    assert actual == expected
    
@pytest.fixture
def tree():
    tree=BinaryTree()
    tree.root=Node(12)
    tree.root.left=Node(4)
    tree.root.right=Node(200)
    tree.root.left.left=Node(17)
    tree.root.left.right=Node(18)
    tree.root.right.left=Node(50)
    tree.pre_order(tree.root)
    return tree