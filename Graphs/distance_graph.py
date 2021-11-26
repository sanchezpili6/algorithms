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


def add_vertex():
    for key, value in estaciones.items():
        print(f"{key} = Vertex('{value['name']}')")
        print(f" metro.add_vertex({key})")


def add_edges():
    for key, value in estaciones.items():
        if len(value['adjacent']) > 0:
            for station in value['adjacent']:
                print(f"metro.add_edge({key}, {station})")


rosario = Vertex('El Rosario')
metro.add_vertex(rosario)
instituto_del_petroleo = Vertex('Instituto del Petroleo')
metro.add_vertex(instituto_del_petroleo)
deportivo_18 = Vertex('Deportivo 18 de Marzo')
metro.add_vertex(deportivo_18)
martin_carrera = Vertex('Martín Carrera')
metro.add_vertex(martin_carrera)
la_raza = Vertex('La Raza')
metro.add_vertex(la_raza)
consulado = Vertex('Consulado')
metro.add_vertex(consulado)
tacuba = Vertex('Tacuba')
metro.add_vertex(tacuba)
guerrero = Vertex('Guerrero')
metro.add_vertex(guerrero)
garibaldi = Vertex('Garibaldi')
metro.add_vertex(garibaldi)
oceania = Vertex('Oceanía')
metro.add_vertex(oceania)
hidalgo = Vertex('Hidalgo')
metro.add_vertex(hidalgo)
bellas_artes = Vertex('Bellas Artes')
metro.add_vertex(bellas_artes)
morelos = Vertex('Morelos')
metro.add_vertex(morelos)
balderas = Vertex('Balderas')
metro.add_vertex(balderas)
salto_del_agua = Vertex('Salto del Agua')
metro.add_vertex(salto_del_agua)
pino_suarez = Vertex('Pino Suarez')
metro.add_vertex(pino_suarez)
san_lazaro = Vertex('San Lázaro')
metro.add_vertex(san_lazaro)
candelaria = Vertex('Candelaria')
metro.add_vertex(candelaria)
tacubaya = Vertex('Tacubaya')
metro.add_vertex(tacubaya)
centro_medico = Vertex('Centro Médico')
metro.add_vertex(centro_medico)
chabacano = Vertex('Chabacano')
metro.add_vertex(chabacano)
jamaica = Vertex('Jamaica')
metro.add_vertex(jamaica)
santa_anita = Vertex('Santa Anita')
metro.add_vertex(santa_anita)
mixcoac = Vertex('Mixcoac')
metro.add_vertex(mixcoac)
zapata = Vertex('Zapata')
metro.add_vertex(zapata)
ermita = Vertex('Ermita')
metro.add_vertex(ermita)
atlalilco = Vertex('Atlalilco')
metro.add_vertex(atlalilco)
pantitlan = Vertex('Pantitlán')
metro.add_vertex(pantitlan)
metro.add_edge(rosario, instituto_del_petroleo)
metro.add_edge(rosario, tacuba)
metro.add_edge(instituto_del_petroleo, la_raza)
metro.add_edge(instituto_del_petroleo, deportivo_18)
metro.add_edge(deportivo_18, la_raza)
metro.add_edge(deportivo_18, martin_carrera)
metro.add_edge(martin_carrera, consulado)
metro.add_edge(la_raza, guerrero)
metro.add_edge(la_raza, consulado)
metro.add_edge(consulado, morelos)
metro.add_edge(consulado, oceania)
metro.add_edge(tacuba, hidalgo)
metro.add_edge(tacuba, tacubaya)
metro.add_edge(guerrero, garibaldi)
metro.add_edge(guerrero, hidalgo)
metro.add_edge(garibaldi, bellas_artes)
metro.add_edge(garibaldi, morelos)
metro.add_edge(oceania, san_lazaro)
metro.add_edge(oceania, pantitlan)
metro.add_edge(hidalgo, bellas_artes)
metro.add_edge(hidalgo, balderas)
metro.add_edge(bellas_artes, salto_del_agua)
metro.add_edge(bellas_artes, pino_suarez)
metro.add_edge(morelos, san_lazaro)
metro.add_edge(morelos, candelaria)
metro.add_edge(balderas, salto_del_agua)
metro.add_edge(balderas, centro_medico)
metro.add_edge(balderas, tacubaya)
metro.add_edge(salto_del_agua, pino_suarez)
metro.add_edge(salto_del_agua, chabacano)
metro.add_edge(pino_suarez, candelaria)
metro.add_edge(pino_suarez, chabacano)
metro.add_edge(san_lazaro, candelaria)
metro.add_edge(san_lazaro, pantitlan)
metro.add_edge(candelaria, jamaica)
metro.add_edge(tacubaya, centro_medico)
metro.add_edge(tacubaya, mixcoac)
metro.add_edge(centro_medico, chabacano)
metro.add_edge(centro_medico, zapata)
metro.add_edge(chabacano, jamaica)
metro.add_edge(chabacano, santa_anita)
metro.add_edge(chabacano, ermita)
metro.add_edge(jamaica, santa_anita)
metro.add_edge(jamaica, pantitlan)
metro.add_edge(santa_anita, atlalilco)
metro.add_edge(mixcoac, zapata)
metro.add_edge(zapata, ermita)
metro.add_edge(ermita, atlalilco)

