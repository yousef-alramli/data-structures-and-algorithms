from code_challenge06 import __version__

from code_challenge06.linked_list import Linked_List , Node
import pytest
def test_version():
    assert __version__ == '0.1.0'



def test_appending_in_end(lil):
    lil.append_to_last("yousef")
    expected = "I am -> 25 -> years -> old -> yousef -> Null"
    actual = lil.__str__()
    print(actual)
    assert expected == actual

def test_appending_before_value(lil):
    lil.append_before(25,"yousef")
    expected = "I am -> yousef -> 25 -> years -> old -> Null"
    actual = lil.__str__()
    assert expected == actual

def test_appending_after_value(lil):
    lil.append_after(25,"yousef")
    expected = "I am -> 25 -> yousef -> years -> old -> Null"
    actual = lil.__str__()
    assert expected == actual




@pytest.fixture
def lil():
    lil = Linked_List()
    lil.append_to_last("I am")
    lil.append_to_last(25)
    lil.append_to_last("years")
    lil.append_to_last("old")
    return lil