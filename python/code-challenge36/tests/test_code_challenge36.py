from code_challenge36 import __version__
from code_challenge36.breadth_first import Vertex ,Graph
import pytest


def test_version():
    assert __version__ == '0.1.0'

def test_breadth_first(graph):
    expected = ['1', '2', '3']
    actual = graph
    assert actual == expected






@pytest.fixture
def graph():
    graph=Graph()
    val1=graph.add_node("1")
    val2=graph.add_node("2")
    val3=graph.add_node("3")
    graph.add_edge(val1,val2,50)
    graph.add_edge(val1,val3,1)
    graph.add_edge(val2,val3,1)

    return graph.bfs(val1)
