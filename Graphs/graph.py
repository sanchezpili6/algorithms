from vertex import Vertex


class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.graph_dict = {}

    def add_vertex(self, vertex):
        # print('Vertex ' + vertex.value + ' added')
        self.graph_dict[vertex.value] = vertex

    def add_edge(self, from_vertex, to_vertex, weight=0):
        # print("Adding edge from " + from_vertex.value + " to " + to_vertex.value)
        self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
        if not self.directed:
            self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)

    def find_path(self, start_vertex, end_vertex):
        start = [start_vertex]
        seen = {}
        while len(start) > 0:
            current_vertex = start.pop(0)
            seen[current_vertex] = True
            # print("Visiting " + current_vertex)
            if current_vertex == end_vertex:
                return True
            else:
                vertex = self.graph_dict[current_vertex]
                next_vertices = vertex.get_edges()

                # Checkpoint 3, uncomment and replace the question marks:
                next_vertices = [vertex for vertex in next_vertices if vertex not in seen]
                start.extend(next_vertices)

        return False
