from heapq import heappop, heappush
from math import inf

metro = {
    'rosario': set([('instituto_del_petroleo', 5), ('tacuba', 3)]),
    'instituto_del_petroleo': set([('la_raza', 1), ('deportivo_18', 1)]),
    'deportivo_18': set([('la_raza', 1), ('martin_carrera', 1)]),
    'martin_carrera': set([('consulado', 2)]),
    'la_raza': set([('guerrero', 1), ('consulado', 2)]),
    'consulado': set([('morelos', 1), ('oceania', 2)]),
    'tacuba': set([('hidalgo', 6), ('tacubaya', 4)]),
    'guerrero': set([('garibaldi', 0), ('hidalgo', 0)]),
    'garibaldi': set([('bellas_artes', 0), ('morelos', 2)]),
    'oceania': set([('san_lazaro', 2), ('pantitlan', 2)]),
    'hidalgo': set([('bellas_artes', 0), ('balderas', 1)]),
    'bellas_artes': set([('salto_del_agua', 1), ('pino_suarez', 2)]),
    'morelos': set([('san_lazaro', 0), ('candelaria', 0)]),
    'balderas': set([('salto_del_agua', 0), ('centro_medico', 2), ('tacubaya', 5)]),
    'salto_del_agua': set([('pino_suarez', 1), ('chabacano', 2)]),
    'pino_suarez': set([('candelaria', 0), ('chabacano', 1)]),
    'san_lazaro': set([('candelaria', 0), ('pantitlan', 5)]),
    'candelaria': set([('jamaica', 1)]),
    'tacubaya': set([('centro_medico', 2), ('mixcoac', 2)]),
    'centro_medico': set([('chabacano', 1), ('zapata', 3)]),
    'chabacano': set([('jamaica', 0), ('santa_anita', 1), ('ermita', 5)]),
    'jamaica': set([('santa_anita', 0), ('pantitlan', 4)]),
    'santa_anita': set([('atlalilco', 5)]),
    'mixcoac': set([('zapata', 2)]),
    'zapata': set([('ermita', 2)]),
    'ermita': set([('atlalilco', 1)]),
    'atlalilco': set([]),
    'pantitlan': set([]),
  }


def dijkstras(graph, start):
    distances = {}

    for vertex in graph:
        distances[vertex] = inf

    distances[start] = 0
    vertices_to_explore = [(0, start)]

    while vertices_to_explore:
        current_distance, current_vertex = heappop(vertices_to_explore)

        for neighbor, edge_weight in graph[current_vertex]:
            new_distance = current_distance + edge_weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heappush(vertices_to_explore, (new_distance, neighbor))

    return distances


distancias_desde_rosario = dijkstras(metro, 'rosario')
print("\n\nDistancias: {0}".format(distancias_desde_rosario))