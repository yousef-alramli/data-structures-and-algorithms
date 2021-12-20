from collections import deque

class Queue:
  def __init__(self):
    self.dq = deque()

  def enqueue(self, value):
    self.dq.append(value)
  
  def dequeue(self):
    return self.dq.pop()
  
  def __len__(self):
    return len(self.dq)

class Vertex:

    def __init__(self,value):
        self.value=value



class Edge:

    def __init__(self,vertex,weight):
        self.vertex = vertex
        self.weight = weight


class Graph:

    def __init__(self) -> None:
        self._adj_list={}

    def add_node(self,value):
        node = Vertex(value)
        self._adj_list[node]=[]

        return node
  
    def add_edge(self,start_vertex,end_vertex,weight =0):
        if start_vertex not in self._adj_list:
            raise KeyError('Start vertex not found in the graph')

        if end_vertex not in self._adj_list:
            raise KeyError('end vertex not found in the graph')

        edge=Edge(end_vertex,weight)
        self._adj_list[start_vertex].append(edge)
  
    def get_neighbors(self, vertex):
        return self._adj_list.get(vertex, [])
    
    def get_nodes(self):
        return self._adj_list.keys()
   
    def size(self):
        return len(self._adj_list)
    
    def bfs(self,start_vertex):

        queue=Queue()
        visited=set()
        result=[]

        queue.enqueue(start_vertex)
        visited.add(start_vertex)
        result.append(start_vertex.value)

        while len(queue):
            current_vertex = queue.dequeue()

            neighbors = self.get_neighbors(current_vertex)

            for edge in neighbors:
                edge = edge.vertex

                if edge not in visited:
                    queue.enqueue(edge)
                    visited.add(edge)
                    result.append(edge.value)
        
        return result
    
def graph_trip_cost(graph, cities):

    trip = False
    next_trip = False
    cost = 0

    for city_index in range(len(cities) - 1):
        neighbors = graph._adj_list[cities[city_index]]
        next_trip = False

        for neighbor in neighbors:
            if cities[city_index + 1] == neighbor.vertex:
                cost += neighbor.weight
                trip = True
                next_trip = True

    trip = trip and next_trip

    if not trip:
        cost = 0

    return f"{trip},${cost}"




if __name__ == "__main__":
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

    print(graph_trip_cost(graph, [pan, are,nar]))