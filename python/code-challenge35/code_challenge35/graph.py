from collections import deque

class Queue:
  def __init__(self):
    self.dq = deque()

  def enqueue(self, value):
    self.dq.append(value)
  
  def dequeue(self):
    return self.dq.pop(0)
  
  def __len__(self):
    return len(self.dq)



class Vertex:

  def __init__(self, value):
    self.value = value

class Edge:

  def __init__(self,vertex, weight):
    self.vertex = vertex
    self.weight = weight

class Graph:

  def __init__(self):
    self.__adj_list = {}
    

  def add_node(self, value):
    node = Vertex(value)
    self.__adj_list[node.value] = []
    return node

  def add_edge(self, start_vertex, end_vertex, weight=0):
    if start_vertex not in self.__adj_list:
      raise KeyError("Start Vertex is not found")
    if end_vertex not in self.__adj_list:
      raise KeyError("Start Vertex is not found")

    edge = Edge(end_vertex, weight)
    self.__adj_list[start_vertex].append(edge)

  def get_neighbors(self, vertex):
    return self.__adj_list.get(vertex, [])
  
  
  def get_nodes(self):
    return self.__adj_list.keys()

 
  def size(self):
    return len(self.__adj_list)



if __name__ == "__main__":
    graph =Graph()
    graph.add_node("1")
    graph.add_node("2")
    graph.add_node("3")
    graph.add_node("4")
    print(graph.get_nodes())
