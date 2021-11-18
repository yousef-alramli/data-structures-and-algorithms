from code_challenge15 import __version__

from code_challenge15.trees import Node , BinaryTree

import pytest

def test_version():
    assert __version__ == '0.1.0'

def test_instantiate_empty_tree():
    tree=BinaryTree()
    expected = []
    actual = tree.pre_order(tree.root)
    assert expected == actual






@pytest.fixture
def tree():
    tree=BinaryTree()
    tree.root=Node("A")
    tree.root.left=Node("B")
    tree.root.right=Node("C")
    tree.root.left.left=Node("D")
    tree.root.left.right=Node("E")
    tree.root.right.left=Node("F")
    return tree
