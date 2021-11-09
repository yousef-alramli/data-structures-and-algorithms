from code_challenge08.linked_list_zip import Linked_List1 , Linked_List2 , zipLists
import pytest

def test_linked_list_zip(lil1,lil2):
    actual = zipLists(lil1,lil2)
    expected = "I am 2 -> I am 1 -> 25.2 -> 25.1 -> years 2 -> years 1 -> old 2 -> old 1 -> Null"
    assert actual == expected

@pytest.fixture
def lil1():
    lil = Linked_List1()
    lil.append("I am 1")
    lil.append(25.1)
    lil.append("years 1")
    lil.append("old 1")
    return lil

@pytest.fixture
def lil2():
    lil = Linked_List2()
    lil.append("I am 2")
    lil.append(25.2)
    lil.append("years 2")
    lil.append("old 2")
    return lil