from code_challenge33 import __version__
from code_challenge33.left_join import left_join
from code_challenge33.hashing import HashTable
import pytest

def test_version():
    assert __version__ == '0.1.0'

def test_left_join(lj):
    expected = [['Alramli', 'al', 'ramli'], ['key', 'ke', 'None'], ['Yosef', 'you', 'sef']]
    actual = lj
    assert expected == actual


@pytest.fixture
def lj():
    hash_table1 = HashTable()
    hash_table1.add("key", "ke")
    hash_table1.add("Yosef", "you")
    hash_table1.add("Alramli", "al")

    hash_table2 = HashTable()
    hash_table2.add("hi", "10")
    hash_table2.add("Yosef", "sef")
    hash_table2.add("Alramli", "ramli")
    
    return left_join(hash_table1 , hash_table2)