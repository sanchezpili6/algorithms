def bfs(graph, start_vertex, target_value):
    path = [start_vertex]
    vertex_and_path = [start_vertex, path]
    bfs_queue = [vertex_and_path]
    visited = set()
    while bfs_queue:
        current_vertex, path = bfs_queue.pop(0)
        visited.add(current_vertex)
        for neighbor in graph[current_vertex]:
            if neighbor not in visited:
                if neighbor is target_value:
                    return path + [neighbor]
                else:
                    bfs_queue.append([neighbor, path + [neighbor]])


metro = {
    'rosario': set(['instituto_del_petroleo', 'tacuba']),
    'instituto_del_petroleo': set(['la_raza', 'deportivo_18']),
    'deportivo_18': set(['la_raza', 'martin_carrera']),
    'martin_carrera': set(['consulado']),
    'la_raza': set(['guerrero', 'consulado']),
    'consulado': set(['morelos', 'oceania']),
    'tacuba': set(['hidalgo', 'tacubaya']),
    'guerrero': set(['garibaldi', 'hidalgo']),
    'garibaldi': set(['bellas_artes', 'morelos']),
    'oceania': set(['san_lazaro', 'pantitlan']),
    'hidalgo': set(['bellas_artes', 'balderas']),
    'bellas_artes': set(['salto_del_agua', 'pino_suarez']),
    'morelos': set(['san_lazaro', 'candelaria']),
    'balderas': set(['salto_del_agua', 'salto_del_agua', 'tacubaya']),
    'salto_del_agua': set(['pino_suarez', 'chabacano']),
    'pino_suarez': set(['candelaria', 'chabacano']),
    'san_lazaro': set(['candelaria', 'pantitlan']),
    'candelaria': set(['jamaica']),
    'tacubaya': set(['centro_medico', 'mixcoac']),
    'centro_medico': set(['chabacano', 'zapata']),
    'chabacano': set(['jamaica', 'santa_anita', 'ermita']),
    'jamaica': set(['santa_anita', 'pantitlan']),
    'santa_anita': set(['atlalilco']),
    'mixcoac': set(['zapata']),
    'zapata': set(['ermita']),
    'ermita': set(['atlalilco']),
    'atlalilco': set([]),
    'pantitlan': set([]),
  }

for estacion in metro:
    print(bfs(metro, 'rosario', estacion))