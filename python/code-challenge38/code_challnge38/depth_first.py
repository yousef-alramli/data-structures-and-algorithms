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

    def depth_first(self,node):
        depth_list = []
        depth_list.append(node.value)

        if node not in self._adj_list:
            return 'Node does not exist'
        elif self._adj_list[node] == []:
            return 'There is no neighbors'

        def adding_to_list(node):
            neighbors = self._adj_list[node]

            for edge in neighbors:
                neighbor = edge.vertex.value

                if neighbor not in depth_list:
                    depth_list.append(neighbor)
                    adding_to_list(edge.vertex)

        adding_to_list(node)

        return depth_list

    
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

    # Pandora=graph.add_node("Pandora")
    # Arendelle=graph.add_node("Arendelle")
    # Metroville=graph.add_node('Metroville')
    # Monstroplolis=graph.add_node('Monstroplolis')
    # Narnia=graph.add_node('Narnia')
    # Naboo=graph.add_node('Naboo')

    # graph.add_edge(Pandora, Arendelle, 150)
    # graph.add_edge(Arendelle, Pandora, 150)

    # graph.add_edge(Arendelle, Metroville, 99)
    # graph.add_edge(Arendelle, Monstroplolis, 42)
    # graph.add_edge(Metroville, Arendelle, 99)
    # graph.add_edge(Monstroplolis, Arendelle,42)

    # graph.add_edge(Metroville, Monstroplolis, 105)
    # graph.add_edge(Monstroplolis, Metroville, 105)
    # graph.add_edge(Metroville, Narnia, 37)
    # graph.add_edge(Narnia, Metroville,37)
    # graph.add_edge(Metroville, Naboo, 26)
    # graph.add_edge(Metroville, Pandora, 82)
    # graph.add_edge(Pandora, Metroville, 82)


    # graph.add_edge(Naboo, Metroville, 26)

    # graph.add_edge(Narnia, Naboo, 250)
    # graph.add_edge(Naboo, Narnia, 250)

    # graph.add_edge(Naboo, Monstroplolis, 73)
    # graph.add_edge(Monstroplolis, Naboo, 73)


    print(graph.depth_first(a))