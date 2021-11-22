from code_challenge17 import __version__
from code_challenge17.breadth import breadth_first
from code_challenge17.trees import BinarySearchTree
import pytest

def test_version():
    assert __version__ == '0.1.0'

def test_breadth_first(tree):
    excepted =  ["A","B","C","D"]
    actual = breadth_first(tree)
    assert excepted == actual

@pytest.fixture
def tree() :
   tree =BinarySearchTree()
   tree.add("A")
   tree.add("B")
   tree.add("C")
   tree.add("D")

   return tree