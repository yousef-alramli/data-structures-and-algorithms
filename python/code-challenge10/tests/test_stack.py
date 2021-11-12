from code_challenge10.stack_and_queue import Node , Stack
import pytest


def test_push(stack):
    actual = stack.top.value
    expected = "yousef"
    assert actual == expected

def test_pop(stack):
    stack.pop()
    actual = stack.top.value
    expected = 3
    assert actual == expected

def test_stac_by_pops(stack):
    stack.pop()
    stack.pop()
    stack.pop()
    actual = stack.top
    expected = None
    assert actual == expected

def test_peek(stack):
    actual = stack.peek()
    expected = "yousef"
    assert actual == expected

def test_is_empty():
    actual = Stack().is_empty()
    expected = True
    assert actual == expected

def test_exeption_empty_stack_peek():
    with pytest.raises(Exception):
        assert Stack().peek()
    
    

def test_exeption_empty_stack_pop():
   with pytest.raises(Exception):
        assert Stack().pop()




@pytest.fixture
def stack():
    stack=Stack()
    stack.push(7)
    stack.push(3)
    stack.push("yousef")
    return stack