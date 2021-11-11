from vertex import Vertex
from graph import Graph

metro = Graph()
estaciones = {
    'rosario': {
        'name': 'El Rosario',
        'adjacent': ['instituto_del_petroleo', 'tacuba']
    },
    'instituto_del_petroleo': {
        'name': 'Instituto del Petroleo',
        'adjacent': ['la_raza', 'deportivo_18']
    },
    'deportivo_18': {
        'name': 'Deportivo 18 de Marzo',
        'adjacent': ['la_raza', 'martin_carrera']
    },
    'martin_carrera': {
        'name': 'Martín Carrera',
        'adjacent': ['consulado']
    },
    'la_raza': {
        'name': 'La Raza',
        'adjacent': ['guerrero', 'consulado']
    },
    'consulado': {
        'name': 'Consulado',
        'adjacent': ['morelos', 'oceania']
    },
    'tacuba': {
        'name': 'Tacuba',
        'adjacent': ['hidalgo', 'tacubaya']
    },
    'guerrero': {
        'name': 'Guerrero',
        'adjacent': ['garibaldi', 'hidalgo']
    },
    'garibaldi': {
        'name': 'Garibaldi',
        'adjacent': ['bellas_artes', 'morelos']
    },
    'oceania': {
        'name': 'Oceanía',
        'adjacent': ['san_lazaro', 'pantitlan']
    },
    'hidalgo': {
        'name': 'Hidalgo',
        'adjacent': ['bellas_artes', 'balderas']
    },
    'bellas_artes': {
        'name': 'Bellas Artes',
        'adjacent': ['salto_del_agua', 'pino_suarez']
    },
    'morelos': {
        'name': 'Morelos',
        'adjacent': ['san_lazaro', 'candelaria']
    },
    'balderas': {
        'name': 'Balderas',
        'adjacent': ['salto_del_agua', 'centro_medico', 'tacubaya']
    },
    'salto_del_agua': {
        'name': 'Salto del Agua',
        'adjacent': ['pino_suarez', 'chabacano']
    },
    'pino_suarez': {
        'name': 'Pino Suarez',
        'adjacent': ['candelaria', 'chabacano']
    },
    'san_lazaro': {
        'name': 'San Lázaro',
        'adjacent': ['candelaria', 'pantitlan']
    },
    'candelaria': {
        'name': 'Candelaria',
        'adjacent': ['jamaica']
    },
    'tacubaya': {
        'name': 'Tacubaya',
        'adjacent': ['centro_medico', 'mixcoac']
    },
    'centro_medico': {
        'name': 'Centro Médico',
        'adjacent': ['chabacano', 'zapata']
    },
    'chabacano': {
        'name': 'Chabacano',
        'adjacent': ['jamaica', 'santa_anita', 'ermita']
    },
    'jamaica': {
        'name': 'Jamaica',
        'adjacent': ['santa_anita', 'pantitlan']
    },
    'santa_anita': {
        'name': 'Santa Anita',
        'adjacent': ['atlalilco']
    },
    'mixcoac': {
        'name': 'Mixcoac',
        'adjacent': ['zapata']
    },
    'zapata': {
        'name': 'Zapata',
        'adjacent': ['ermita']
    },
    'ermita': {
        'name': 'Ermita',
        'adjacent': ['atlalilco']
    },
    'atlalilco': {
        'name': 'Atlalilco',
        'adjacent': []
    },
    'pantitlan': {
        'name': 'Pantitlán',
        'adjacent': []
    }
}

for key, value in estaciones.items():
    key = Vertex(value['name'])
    metro.add_vertex(key)

