from code_challenge37 import __version__
from code_challenge37.trip import Graph, Vertex, Edge, graph_trip_cost
import pytest


def test_version():
    assert __version__ == '0.1.0'

def test_one_true_trip(trip):

    actual = graph_trip_cost(trip[0], [trip[1],trip[2]])
    expected = "True,$150"
    assert actual == expected

def test_false_trip(trip):

    actual = graph_trip_cost(trip[0], [trip[1],trip[2],trip[3]])
    expected = 'False,$0'
    assert actual == expected

def test_more_than_one_trip(trip):

    actual = graph_trip_cost(trip[0], [trip[1],trip[2],trip[4]])
    expected = 'True,$192'
    assert actual == expected


@pytest.fixture
def trip():
    graph = Graph()

    pan = graph.add_node('Pandora')
    nab = graph.add_node('Naboo')
    nar = graph.add_node('Narnia')
    mon = graph.add_node('Monstroplolis')
    are = graph.add_node('Arendelle')
    met = graph.add_node('Metroville')

    graph.add_edge(pan, are, 150)
    graph.add_edge(pan, met, 82)
    graph.add_edge(are, pan, 150)
    graph.add_edge(are, met, 99)
    graph.add_edge(are, mon, 42)
    graph.add_edge(met, pan, 82)
    graph.add_edge(met, are, 99)
    graph.add_edge(met, mon, 105)
    graph.add_edge(met, nab, 26)
    graph.add_edge(met, nar, 37)
    graph.add_edge(mon, are, 42)
    graph.add_edge(mon, met, 105)
    graph.add_edge(mon, nab, 73)
    graph.add_edge(nab, mon, 73)
    graph.add_edge(nab, met, 26)
    graph.add_edge(nab, nar, 250)
    graph.add_edge(nar, met, 37)
    graph.add_edge(nar, nab, 250)

    return graph , pan, are, nab ,mon