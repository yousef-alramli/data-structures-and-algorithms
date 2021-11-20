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

def test_single_root():
    tree=BinaryTree()
    tree.root=Node("A")
    expected = ["A"]
    actual = tree.pre_order(tree.root)
    assert expected == actual

def test_add_left_right():
    tree=BinaryTree()
    tree.root=Node("A")
    tree.root.left=Node("B")
    tree.root.right=Node("C")
    expected = ["A","B","C"]
    actual = tree.pre_order(tree.root)
    assert expected == actual

def test_pre_order(tree):
    expected = ['A', 'B', 'D', 'E', 'C', 'F']
    actual = tree.pre_order(tree.root)
    assert expected == actual

def test_in_order(tree):
    expected = ['D', 'B', 'E', 'A', 'F', 'C']
    actual = tree.in_order(tree.root)
    assert expected == actual

def test_post_order(tree):
    expected = [ 'D', 'E', 'B', 'F', 'C', 'A']
    actual = tree.post_order(tree.root)
    assert expected == actual


@pytest.fixture
def tree():
    tree=BinaryTree()
    tree.output = []
    tree.root=Node("A")
    tree.root.left=Node("B")
    tree.root.right=Node("C")
    tree.root.left.left=Node("D")
    tree.root.left.right=Node("E")
    tree.root.right.left=Node("F")
    return tree
