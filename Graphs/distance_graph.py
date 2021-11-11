from vertex import Vertex
from graph import Graph

# definir al grafo Metro
metro = Graph()

# definir estaciones

estaciones = {
    'rosario': 'El Rosario',
    'instituto_del_petroleo': 'Instituto del Petroleo',
    'deportivo_18': 'Deportivo 18 de Marzo',
    'martin_carrera': 'Martín Carrera',
    'la_raza': 'La Raza',
    'consulado': 'Consulado',
    'tacuba': 'Tacuba',
    'guerrero': 'Guerrero',
    'garibaldi': 'Garibaldi',
    'oceania': 'Oceanía',
    'hidalgo': 'Hidalgo',
    'bellas_artes': 'Bellas Artes',
    'morelos': 'Morelos',
    'balderas': 'Balderas',
    'salto_del_agua': 'Salto del Agua',
    'pino_suarez': 'Pino Suarez',
    'san_lazaro': 'San Lázaro',
    'candelaria': 'Candelaria',
    'tacubaya': 'Tacubaya',
    'centro_medico': 'Centro Médico',
    'chabacano': 'Chabacano',
    'jamaica': 'Jamaica',
    'santa_anita': 'Santa Anita',
    'mixcoac': 'Mixcoac',
    'zapata': 'Zapata',
    'ermita': 'Ermita',
    'atlalilco': 'Atlalilco',
    'pantitlan': 'Pantitlán',
}

# crear vertices por estaciones

for key, value in estaciones.items():
    key = Vertex(value)

# Agregar vértices de estaciones al grafo metro

for key, value in estaciones.items():
    print(key)
    metro.add_vertex(key)
