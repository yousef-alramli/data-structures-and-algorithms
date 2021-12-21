from code_challnge38 import __version__
from code_challnge38.depth_first import Graph, Vertex, Edge
import pytest


def test_version():
    assert __version__ == '0.1.0'


def test_depth(df):
    actual = df[0].depth_first(df[1])
    expected = ['a', 'b', 'c', 'g', 'd', 'e', 'h', 'f']
    assert actual == expected

def test_depth_one_node():
    graph = Graph()
    a = graph.add_node('a')
    actual = graph.depth_first(a)
    expected = 'There is no neighbors'
    assert actual == expected

def test_depth_not_existing_node():
    graph1 = Graph()
    graph2 = Graph()
    a = graph1.add_node('a')
    b = graph2.add_node('b')
    actual = graph1.depth_first(b)
    expected = 'Node does not exist'
    assert actual == expected



@pytest.fixture
def df():
    graph = Graph()

    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    d = graph.add_node('d')
    e = graph.add_node('e')
    f = graph.add_node('f')
    g = graph.add_node('g')
    h = graph.add_node('h')


    graph.add_edge(a, b, 82)
    graph.add_edge(a, d, 150)

    graph.add_edge(b, c, 99)
    graph.add_edge(b, d, 150)

    graph.add_edge(c, g, 42)
    graph.add_edge(g, c, 82)

    graph.add_edge(d, e, 42)
    graph.add_edge(d, h, 37)
    graph.add_edge(d, f, 26)
    graph.add_edge(d, a, 99)
    graph.add_edge(d, b, 105)

    graph.add_edge(f, d, 105)
    graph.add_edge(f, h, 73)

    graph.add_edge(h, d, 73)
    graph.add_edge(h, f, 26)

    graph.add_edge(e, d, 250)

    return graph ,a