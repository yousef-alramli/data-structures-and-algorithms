from code_challenge35 import __version__
from code_challenge35.graph import Graph ,Vertex ,Edge
import pytest


def test_version():
    assert __version__ == '0.1.0'

def test_add_and_get_node(gra):
    expect = "dict_keys(['1', '2', '3', '4'])"
    actual = f"{gra.get_nodes()}"
    assert actual == expect

def test_add_node(gra):
    expect = "dict_keys(['1', '2', '3', '4'])"
    actual = f"{gra.get_nodes()}"
    assert actual == expect

def test_size_empty():
    graph = Graph()
    expected = 0
    actual = graph.size()
    assert actual == expected

def test_size(gra):
    expected = 4
    actual = gra.size()
    assert actual == expected

def test_add_edge_interloper_start():

    graph = Graph()

    start = Vertex('start')

    end = graph.add_node('end')

    with pytest.raises(KeyError):
        graph.add_edge(start, end)

def test_add_edge_interloper_end():

    graph = Graph()

    end = Vertex('end')

    start = graph.add_node('start')

    with pytest.raises(KeyError):

        graph.add_edge(start, end)





@pytest.fixture
def gra():
    graph = Graph()
    graph.add_node("1")
    graph.add_node("2")
    graph.add_node("3")
    graph.add_node("4")
    return graph




