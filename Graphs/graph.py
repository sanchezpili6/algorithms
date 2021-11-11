from vertex import Vertex


class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.graph_dict = {}

    def add_vertex(self, vertex):
        print('Vertex ' + vertex + ' added')
        self.graph_dict[vertex.value] = vertex

