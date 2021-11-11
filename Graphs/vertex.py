class Vertex:
    def __init__(self, value):
        print('Vertex ' + value + ' created')
        self.value = value
        self.edges = {}

    def get_edges(self):
        return list(self.edges.keys())

    def add_edge(self, vertex):
        print("Adding " + vertex)
        self.edges[vertex] = True
