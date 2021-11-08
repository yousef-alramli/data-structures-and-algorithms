from code_challenge07.linked_list import Linked_List
import pytest

def test_k_is_greater_than_len(lil):   
    actual = lil.kthFromEnd(6)
    expected = "Exception"
    assert actual == expected


def test_k_is_equal_len(lil):
    actual = lil.kthFromEnd(6)
    expected = "Exception"
    assert actual == expected

def test_k_is_not_positive_int(lil):
    actual = lil.kthFromEnd(-1)
    expected = "Exception"
    assert actual == expected

def test_k_is_of_size_one():
    lil = Linked_List()
    lil.append_to_last("I am")
    actual = lil.kthFromEnd(0)
    expected = "I am"
    assert actual == expected

def test_happy_path(lil):
    actual = lil.kthFromEnd(2)
    expected = 25
    assert actual == expected

@pytest.fixture
def lil():
    lil = Linked_List()
    lil.append_to_last("I am")
    lil.append_to_last(25)
    lil.append_to_last("years")
    lil.append_to_last("old")
    return lil