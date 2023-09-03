from graph import Graph

def main():
    test_graph_print()
    test_graph_num_vertices()
    test_graph_num_edges()
    test_graph_contains_edge()
    test_bfs_basic()
    test_bfs_small_graphs()
    test_bfs_large_graph()
    test_dfs_basic()
    test_dfs_large_graph()

def test_graph_print():
    graph = Graph(5)
    graph.add_edge(2, 3, 5)
    graph.print_graph()
    graph.rmv_edge(2, 3)
    print()
    graph.print_graph()
    print()

    graph = Graph(8)
    graph.add_edge(0, 1, 8)
    graph.add_edge(0, 3, 2)
    graph.add_edge(2, 3, 1)
    graph.add_edge(2, 5, 6)
    graph.add_edge(1, 2, 3)
    graph.add_edge(2, 1, 3)
    graph.add_edge(3, 6, 7)
    graph.add_edge(4, 7, 22)
    graph.add_edge(4, 0, 9)
    graph.add_edge(5, 3, 19)
    graph.add_edge(6, 7, 12)
    graph.add_edge(6, 2, 11)
    graph.add_edge(7, 2, 11)
    graph.add_edge(7, 0, 133)
    graph.add_edge(7, 5, 22)
    graph.add_edge(4, 7, 12)
    graph.add_edge(8, 2, 11)
    graph.print_graph()
    print()
    graph.rmv_edge(4, 7)
    graph.rmv_edge(7, 4)
    graph.rmv_edge(3, 6)
    graph.rmv_edge(4, 1)
    graph.print_graph()
    print()

    graph = Graph(10)
    graph.print_graph()
    print()
    graph.rmv_edge(9, 1)
    graph.print_graph()
    print()
    graph.add_edge(1, 33, 2)
    graph.print_graph()
    print()

    graph = Graph(0)
    graph.print_graph()
    print()

    graph = Graph(1)
    graph.print_graph()

def test_graph_num_vertices():
    graph = Graph(5)
    assert(graph.nV == 5)
    graph.add_edge(2, 3, 5)
    assert(graph.nV == 5)
    graph.rmv_edge(2, 3)
    assert(graph.nV == 5)

    graph = Graph(8)
    assert(graph.nV == 8)

    for i in range(20):
        graph = Graph(i)
        assert(graph.nV == i)

def test_graph_num_edges():
    graph = Graph(5)
    assert(graph.nE == 0)
    graph.add_edge(2, 3, 5)
    assert(graph.nE == 1)
    graph.rmv_edge(2, 3)
    assert(graph.nE == 0)

    graph = Graph(8)
    assert(graph.nE == 0)
    graph.add_edge(0, 1, 8)
    graph.add_edge(0, 3, 2)
    graph.add_edge(2, 3, 1)
    graph.add_edge(2, 5, 6)
    assert(graph.nE == 4)
    graph.add_edge(1, 2, 3)
    graph.add_edge(2, 1, 3)
    graph.add_edge(3, 6, 7)
    assert(graph.nE == 7)
    graph.add_edge(4, 7, 22)
    graph.add_edge(4, 0, 9)
    assert(graph.nE == 9)
    graph.add_edge(5, 3, 19)
    graph.add_edge(6, 7, 12)
    graph.add_edge(6, 2, 11)
    assert(graph.nE == 12)
    graph.add_edge(7, 2, 11)
    graph.add_edge(7, 0, 133)
    graph.add_edge(7, 5, 22)
    assert(graph.nE == 15)
    graph.add_edge(4, 7, 12)
    assert(graph.nE == 15)
    graph.rmv_edge(4, 7)
    graph.rmv_edge(7, 4)
    assert(graph.nE == 14)
    graph.rmv_edge(3, 6)
    assert(graph.nE == 13)
    graph.rmv_edge(4, 1)
    assert(graph.nE == 13)

def test_graph_contains_edge():
    graph = Graph(5)
    graph.add_edge(2, 3, 5)
    assert(graph.contains_edge(2, 3) == True)
    assert(graph.contains_edge(3, 2) == False)
    graph.rmv_edge(2, 3)
    assert(graph.contains_edge(2, 3) == False)
    assert(graph.contains_edge(3, 2) == False)

    graph = Graph(8)
    graph.add_edge(0, 1, 8)
    graph.add_edge(0, 3, 2)
    graph.add_edge(2, 3, 1)
    graph.add_edge(2, 5, 6)
    graph.add_edge(1, 2, 3)
    graph.add_edge(2, 1, 3)
    graph.add_edge(3, 6, 7)
    graph.add_edge(4, 7, 22)
    graph.add_edge(4, 0, 9)
    graph.add_edge(5, 3, 19)
    graph.add_edge(6, 7, 12)
    graph.add_edge(6, 2, 11)
    graph.add_edge(7, 2, 11)
    graph.add_edge(7, 0, 133)
    graph.add_edge(7, 5, 22)
    graph.add_edge(4, 7, 12)
    assert(graph.contains_edge(3, 2) == False)
    assert(graph.contains_edge(2, 3) == True)
    assert(graph.contains_edge(0, 1) == True)
    assert(graph.contains_edge(1, 0) == False)
    assert(graph.contains_edge(0, 7) == False)
    assert(graph.contains_edge(7, 0) == True)
    assert(graph.contains_edge(2, 1) == True)
    assert(graph.contains_edge(5, 3) == True)
    graph.rmv_edge(4, 7)
    graph.rmv_edge(7, 4)
    graph.rmv_edge(3, 6)
    assert(graph.contains_edge(4, 1) == False)
    graph.rmv_edge(4, 1)
    assert(graph.contains_edge(4, 7) == False)
    assert(graph.contains_edge(7, 4) == False)
    assert(graph.contains_edge(3, 6) == False)
    assert(graph.contains_edge(4, 1) == False)

def test_bfs_basic():
    graph = Graph(4)
    graph.add_edge(0, 1, 1)
    graph.add_edge(0, 2, 1)
    graph.add_edge(1, 2, 1)
    graph.add_edge(2, 0, 1)
    graph.add_edge(2, 3, 1)
    graph.add_edge(3, 3, 1)

    path = graph.bfs(2, 3)
    assert path == [2, 3]

    path = graph.bfs(0, 3)
    assert path == [0, 2, 3]

    path = graph.bfs(3, 0)
    assert path == []

def test_bfs_small_graphs():
    # One vertex
    graph = Graph(1)
    path = graph.bfs(0, 0)
    assert path == [0]

    # Disconnected vertices
    graph = Graph(2)
    path = graph.bfs(0, 1)
    assert path == []

    graph = Graph(2)
    graph.add_edge(0, 1, 1)
    path = graph.bfs(0, 1)
    assert path == [0, 1]

    graph = Graph(4)
    graph.add_edge(0, 1, 1)
    graph.add_edge(0, 2, 1)
    graph.add_edge(1, 3, 1)
    graph.add_edge(2, 3, 1)

    path = graph.bfs(0, 3)
    assert path == [0, 1, 3] or path == [0, 2, 3]

    # cycles
    graph = Graph(4)
    graph.add_edge(0, 1, 1)
    graph.add_edge(1, 2, 1)
    graph.add_edge(2, 3, 1)
    graph.add_edge(3, 0, 1)

    path = graph.bfs(0, 3)
    assert path == [0, 1, 2, 3]

def test_bfs_large_graph():
    graph = Graph(25)

    # Add edges to the graph
    graph.add_edge(0, 1, 1)
    graph.add_edge(0, 2, 1)
    graph.add_edge(1, 3, 1)
    graph.add_edge(2, 4, 1)
    graph.add_edge(3, 5, 1)
    graph.add_edge(4, 6, 1)
    graph.add_edge(5, 7, 1)
    graph.add_edge(6, 8, 1)
    graph.add_edge(7, 9, 1)
    graph.add_edge(8, 10, 1)
    graph.add_edge(9, 11, 1)
    graph.add_edge(10, 12, 1)
    graph.add_edge(11, 13, 1)
    graph.add_edge(12, 14, 1)
    graph.add_edge(13, 15, 1)
    graph.add_edge(14, 16, 1)
    graph.add_edge(15, 17, 1)
    graph.add_edge(16, 18, 1)
    graph.add_edge(17, 19, 1)
    graph.add_edge(18, 20, 1)
    graph.add_edge(19, 21, 1)
    graph.add_edge(20, 22, 1)
    graph.add_edge(21, 23, 1)
    graph.add_edge(22,24 ,1)

    assert graph.bfs(0 ,24) == [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
    assert graph.bfs(24, 22) == []
    assert graph.bfs(24, 0) == []
    assert graph.bfs(3, 23) == [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]

def test_dfs_basic():
    graph = Graph(1)
    path = graph.dfs(0, 0)
    assert path == [0]

    graph = Graph(2)
    path = graph.dfs(0, 1)
    assert path == []

    graph = Graph(2)
    graph.add_edge(0, 1, 1)
    path = graph.dfs(0, 1)
    assert path == [0, 1]

    graph = Graph(4)
    graph.add_edge(0, 1, 1)
    graph.add_edge(0, 2, 1)
    graph.add_edge(1, 3, 1)
    graph.add_edge(2, 3, 1)

    path = graph.dfs(0, 3)
    assert path == [0, 1, 3] or path == [0, 2, 3]

def test_dfs_large_graph():
    graph = Graph(25)

    graph.add_edge(0, 1, 1)
    graph.add_edge(0, 2, 1)
    graph.add_edge(1, 3, 1)
    graph.add_edge(2, 4, 1)
    graph.add_edge(3, 5, 1)
    graph.add_edge(4, 6, 1)
    graph.add_edge(5, 7, 1)
    graph.add_edge(6, 8, 1)
    graph.add_edge(7, 9, 1)
    graph.add_edge(8, 10, 1)
    graph.add_edge(9, 11, 1)
    graph.add_edge(10, 12, 1)
    graph.add_edge(11, 13, 1)
    graph.add_edge(12, 14, 1)
    graph.add_edge(13, 15, 1)
    graph.add_edge(14, 16, 1)
    graph.add_edge(15, 17, 1)
    graph.add_edge(16, 18, 1)
    graph.add_edge(17, 19, 1)
    graph.add_edge(18, 20, 1)
    graph.add_edge(19, 21, 1)
    graph.add_edge(20, 22, 1)
    
    assert graph.dfs(0, 22) == [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]
    assert graph.dfs(19, 0) == []
    assert graph.dfs(12, 1) == []
    assert graph.dfs(20, 22) == [20, 22]

def test_dijkstra_basic():
    graph = Graph(5)
    graph.add_edge(0, 1, 2)
    graph.add_edge(0, 3, 1)
    graph.add_edge(1, 2, 3)
    graph.add_edge(2, 4, 5)
    graph.add_edge(3, 4, 4)

    assert graph.dijkstras(0, 4) == [0, 3, 4]

    graph = Graph(5)
    graph.add_edge(0, 1, 2)
    graph.add_edge(1, 2, 3)

    assert graph.dijkstras(0, 4) == []

    graph = Graph(5)
    graph.add_edge(0, 1, 2)
    graph.add_edge(0, 3, 1)
    graph.add_edge(1, 2, 3)
    graph.add_edge(2, 4, 5)
    graph.add_edge(3, 4, 9)

    assert graph.dijkstras(0, 4) in [[0, 1 ,2 ,4], [0 ,3 ,4]]

def test_dijkstras_large_graph():
    graph = Graph(10)
    graph.add_edge(0, 1, 2)
    graph.add_edge(0, 3, 1)
    graph.add_edge(1, 2, 3)
    graph.add_edge(2, 4, 5)
    graph.add_edge(3, 4, 4)
    graph.add_edge(4, 5, 6)
    graph.add_edge(5, 6, 7)
    graph.add_edge(6, 7, 8)
    graph.add_edge(7, 8, 9)
    graph.add_edge(8, 9, 10)
    graph.add_edge(9, 0, 11)
    graph.add_edge(1, 5, 12)
    graph.add_edge(2, 6, 13)
    graph.add_edge(3, 7, 14)
    graph.add_edge(4, 8, 15)

    assert graph.dijkstras(0, 9) in [[0 ,1 ,2 ,4 ,5 ,6 ,7 ,8 ,9], [0 ,3 ,4 ,5 ,6 ,7 ,8 ,9], [0 ,3 ,7 ,8 ,9]]


if __name__ == "__main__":
    main()