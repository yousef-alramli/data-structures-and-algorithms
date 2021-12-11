from code_challenge30 import __version__
from code_challenge30.hash import HashTable
import pytest
from code_challenge30.ll import Node , LinkedList


def test_version():
    assert __version__ == '0.1.0'

def test_add(hashed):
    actual = hashed[0]
    expected = ["['key', 10] -> ['eky', 10] -> ['yek', 10] -> Null", 20, 20]
    assert actual == expected

def test_contains(hashed):

    assert hashed[1].contains("sos") == True
    assert hashed[1].contains("oss") == False

def test_get(hashed):

    assert hashed[1].get("sos") == 20
    

@pytest.fixture
def hashed():
    hash_table = HashTable()
    hash_table.add("key", 10)
    hash_table.add("yo", 20)
    hash_table.add("sos", 20)
    hash_table.add("eky", 10)
    hash_table.add("yek", 10)
    arr = []
    for i,item in enumerate(hash_table.map):
        if item:
            if isinstance(item, LinkedList):
                arr.append(item.__str__())
            else:
                arr.append(item)
    
    return arr , hash_table