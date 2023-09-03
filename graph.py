from queue import Queue
from stack import Stack
from pqueue import PQueue
from typing import List
import sys

class Graph:
    """
    Initialises a new Graph object with nV vertices
    @param nV: number of vertices
    """
    def __init__(self, nV: int):
        try:
            self.nV = nV
        except ValueError as err:
            print(err, "so num vertices is set to default value (10)")
            self.nV = 10
        
        self.nE = 0

        self.list = []
        for _ in range(nV):
            self.list.append([])

    """
    Checks if the given vertices are within the bounds of the graph
    @param v1: the first vertex
    @param v2: the second vertex
    """
    def vertex_in_bounds(self, v1: int, v2: int) -> None:
        if (v1 < 0 or v2 < 0 or v1 >= self.nV or v2 >= self.nV):
            raise ValueError(f"Vertices {v1} and {v2} must be between 0 and {self.nV - 1}")

    """
    Adds an edge between the specified vertices with the given weight
    @param src: the source vertex
    @param dest: the destination vertex
    @param weight: the weight of the edge
    """
    def add_edge(self, src: int, dest: int, weight: int) -> None:
        try:
            self.vertex_in_bounds(src, dest)
        except ValueError as err:
            print(err)
            return
        
        for edge in self.list[src]:
            if edge["to"] == dest:
                return
        
        self.list[src].append({"to": dest, "weight": weight})
        self.nE = self.nE + 1

    """
    If an edge exists between the specified vertices, removes it
    @param src: the source vertex
    @param dest: the destination vertex
    """
    def rmv_edge(self, src: int, dest: int) -> None:
        try:
            self.vertex_in_bounds(src, dest)
        except ValueError as err:
            print(err)
            return
        
        for i, edge in enumerate(self.list[src]):
            if edge["to"] == dest:
                del self.list[src][i]
                self.nE = self.nE - 1
                return
            
        print("No edge between src and dest was found")

    """
    Prints the graph
    """
    def print_graph(self) -> None:
        for i, vertex in enumerate(self.list):
            print(f"{i} has edges to: ", end="")
            for edge in vertex:
                print(f"{edge['to']} ", end="")
            print()

    """Returns the number of vertices in the graph."""
    @property
    def nV(self) -> int:
        return self._nV
    
    """Sets the number of vertices in the graph."""
    @nV.setter
    def nV(self, value: int) -> None:
        if value < 0:
            raise ValueError("The number of vertices should be greater than 0")
        
        self._nV = value
    
    """Returns the number of edges in the graph."""
    @property
    def nE(self):
        return self._nE
    
    """Sets the number of edges in the graph."""
    @nE.setter
    def nE(self, value: int) -> None:
         if value < 0:
             raise ValueError("The number of edges must be greater than 0")
         self._nE = value
    
    """
    Checks if there is an edge from the source to the destination vertex
    @param src: the source vertex
    @param dest: the destination vertex
    """
    def contains_edge(self, src: int, dest: int) -> bool:
        for edge in self.list[src]:
            if edge["to"] == dest:
                return True

        return False

    """
    Finds a path from the source to the destination vertex using a Breadth First Search.
    @param src: the source vertex
    @param dest: the destination vertex
    """
    def bfs(self, src: int, dest: int) -> List[int]:
        try:
            self.vertex_in_bounds(src, dest)
        except ValueError as err:
            print(err)
            return
        # setup
        visited = [-1 for _ in range(self.nV)]
        visited[src] = src
        q = Queue()
        q.enqueue(src, src, 0)

        while not q.is_empty():
            edge = q.dequeue()
            if edge["to"] == dest:
                break
            
            # visit each of the current vertex's neighbours
            for vertex in self.list[edge["to"]]:
                if visited[vertex["to"]] == -1:
                    visited[vertex["to"]] = edge["to"]
                    q.enqueue(edge["to"], vertex["to"], vertex["weight"])

        if visited[dest] == -1: 
            print("Destination vertex is not reachable from source vertex")
            return []

        # store the path from src to dest
        i = dest
        path = []
        while (i != src):
            path.append(i)
            i = visited[i]
        path.append(src)
        path.reverse()

        print("The path from the source to the destination vertex is: ", end=" ")
        for i in range(len(path)):
            print(path[i], end=" ")
        print()

        return path

    """
    Finds a path from the source to the destination vertex using a Depth First Search.
    @param src: the source vertex
    @param dest: the destination vertex
    """
    def dfs(self, src: int, dest: int) -> List[int]:
        try:
            self.vertex_in_bounds(src, dest)
        except ValueError as err:
            print(err)
            return
        
        # setup
        visited = [0 for _ in range(self.nV)]
        pred = [-1 for _ in range(self.nV)]
        pred[src] = src
        s = Stack()
        s.push(src, src, 0)

        while not s.is_empty():
            edge = s.pop()
            if visited[edge["to"]]:
                continue
            
            visited[edge["to"]] = 1
            found = False
            for vertex in self.list[edge["to"]]:
                if pred[vertex["to"]] == -1:
                    s.push(edge["to"], vertex["to"], vertex["weight"])
                    pred[vertex["to"]] = edge["to"]
                    if vertex["to"] == dest:
                        found = True

            if found == True:
                break

        if pred[dest] == -1:
            print("Destination vertex is not reachable from source vertex")
            return []
        
        i = dest
        path = []
        while (i != src):
            path.append(i)
            i = pred[i]
        path.append(src)
        path.reverse()

        print("The path from the source to the destination vertex is: ", end=" ")
        for i in range(len(path)):
            print(path[i], end=" ")
        print()

        return path

    """
    Finds the shortest path from the source to the destination vertex
    using Dijkstra's algorithm
    @param src: the source vertex
    @param dest: the destination vertex
    """
    def dijkstras(self, src: int, dest: int) -> List[int]:
        try:
            self.vertex_in_bounds(src, dest)
        except ValueError as err:
            print(err)
            return
        
        print("TODO")
        
    """
    Finds a minimum spanning tree of the graph using Prim's algorithm
    Assumes the graph is connected
    """
    def prims(self) -> None:
        print("TODO")

    """
    Finds a minimum spanning tree of the graph using Kruskal's algorithm.
    Assumes the graph is connected.
    """
    def kruskals(self) -> None:
        print("TODO")
