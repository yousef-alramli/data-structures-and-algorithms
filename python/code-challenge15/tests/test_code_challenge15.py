from code_challenge15 import __version__

from code_challenge15.trees import Node , BinaryTree , BinarySearchTree

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

def test_BTS_contain(BTS):
    assert BTS.contain(5) == False
    assert BTS.contain(23) == True

def test_BTS_add(BTS):
    assert BTS.root.left.value == 14
    assert BTS.root.right.value == 23
    assert BTS.root.value == 15


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

@pytest.fixture
def BTS():
    search_tree = BinarySearchTree()
    search_tree.add(15)
    search_tree.add(14)
    search_tree.add(4)
    search_tree.add(23)
    return search_tree

