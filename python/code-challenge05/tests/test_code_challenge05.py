from code_challenge05 import __version__
from code_challenge05.node import Node , Linked_In_List
import pytest

def test_version():
    assert __version__ == '0.1.0'

def test_empty_list():
    expected = "Null"
    actual = Linked_In_List().__str__()
    assert expected == actual

def test_full_list(lil):
    expected = "I am -> 25 -> years -> old -> Null"
    actual = lil.__str__()
    assert expected == actual

def test_head_is_first_node(lil):
    expected = "I am"
    actual = lil.head.value
    assert expected == actual

def test_true_if_value_inside(lil):
    boolean = False
    if "years" in lil.__str__():
        boolean = True
        return boolean
    return boolean
    assert boolean == True

def test_false_if_value_inside(lil):
    boolean = True
    if "Hello" in lil.__str__():
        boolean = False
        return boolean
    return boolean
    assert boolean == False



@pytest.fixture
def lil():
    lil = Linked_In_List()
    lil.appending("I am")
    lil.appending(25)
    lil.appending("years")
    lil.appending("old")
    return lil