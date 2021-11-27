from vertex import Vertex


class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.graph_dict = {}

    def add_vertex(self, vertex):
        print('Vertex ' + vertex.value + ' added')
        self.graph_dict[vertex.value] = vertex

    def add_edge(self, from_vertex, to_vertex):
        print("Adding edge from " + from_vertex.value + " to " + to_vertex.value)
        self.graph_dict[from_vertex.value].add_edge(to_vertex.value)
        if not self.directed:
            self.graph_dict[to_vertex.value].add_edge(from_vertex.value)