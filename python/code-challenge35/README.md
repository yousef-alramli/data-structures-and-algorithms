# Graphs

a graph is an abstract data type that is meant to implement the undirected graph and directed graph.

## Challenge

create a graph class to Implement methods in how to add node , add edge , get nodes , get neighbors and size .

## Approach & Efficiency

The Efficiency of the Big O time is O(n)
The Efficiency of the Big O space is O(n)

## API

1. **add node**

    Arguments: value
    Returns: The added node
    Add a node to the graph

-    Big O time is O(1)
-    Big O space is O(1)

2. **add edge**

    Arguments: 2 nodes to be connected by the edge, weight (optional)
    Returns: nothing
    Adds a new edge between two nodes in the graph, If specified, assign a weight to the edge, Both nodes should already be in the Graph

-    Big O time is O(1)
-    Big O space is O(1)

3. **get nodes**

    Arguments: none
    Returns all of the nodes in the graph as a collection (set, list, or similar)

-    Big O time is O(n)
-    Big O space is O(n)

4. **get neighbors**

    Arguments: node
    Returns a collection of edges connected to the given node Include the weight of the connection in the returned collection

-    Big O time is O(1)
-    Big O space is O(n)

5. **size**

    Arguments: none
    Returns the total number of nodes in the graph

-    Big O time is O(1)
-    Big O space is O(1)