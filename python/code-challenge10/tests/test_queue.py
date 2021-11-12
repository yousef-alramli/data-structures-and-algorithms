from code_challenge10.stack_and_queue import Node , Queue
import pytest


def test_enqueue(queue):
    actual = queue.rear.value
    expected = "yousef"
    assert actual == expected

def test_dequeue(queue):
    queue.dequeue()
    actual = queue.front.value
    expected = 3
    assert actual == expected

def test_stac_by_dequeues(queue):
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    actual = queue.front
    expected = None
    assert actual == expected

def test_peek(queue):
    actual = queue.peek().value
    expected = 7
    assert actual == expected

def test_is_empty():
    actual = Queue().is_empty()
    expected = True
    assert actual == expected

def test_exeption_empty_queue_peek():
    with pytest.raises(Exception):
        assert Queue().peek()
    
    

def test_exeption_empty_queue_dequeue():
   with pytest.raises(Exception):
        assert Queue().dequeue()




@pytest.fixture
def queue():
    queue=Queue()
    queue.enqueue(7)
    queue.enqueue(3)
    queue.enqueue("yousef")
    return queue