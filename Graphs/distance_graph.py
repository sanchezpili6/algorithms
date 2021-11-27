from vertex import Vertex
from graph import Graph

metro = Graph()
estaciones = {
    'rosario': {
        'name': 'El Rosario',
        'adjacent': [('instituto_del_petroleo', 5), ('tacuba', 3)]
    },
    'instituto_del_petroleo': {
        'name': 'Instituto del Petroleo',
        'adjacent': [('la_raza', 1), ('deportivo_18', 1)]
    },
    'deportivo_18': {
        'name': 'Deportivo 18 de Marzo',
        'adjacent': [('la_raza', 1), ('martin_carrera', 1)]
    },
    'martin_carrera': {
        'name': 'Martín Carrera',
        'adjacent': [('consulado', 2)]
    },
    'la_raza': {
        'name': 'La Raza',
        'adjacent': [('guerrero', 1), ('consulado', 2)]
    },
    'consulado': {
        'name': 'Consulado',
        'adjacent': [('morelos', 1), ('oceania', 2)]
    },
    'tacuba': {
        'name': 'Tacuba',
        'adjacent': [('hidalgo', 6), ('tacubaya', 4)]
    },
    'guerrero': {
        'name': 'Guerrero',
        'adjacent': [('garibaldi', 0), ('hidalgo', 0)]
    },
    'garibaldi': {
        'name': 'Garibaldi',
        'adjacent': [('bellas_artes', 0), ('morelos', 2)]
    },
    'oceania': {
        'name': 'Oceanía',
        'adjacent': [('san_lazaro', 2), ('pantitlan', 2)]
    },
    'hidalgo': {
        'name': 'Hidalgo',
        'adjacent': [('bellas_artes', 0), ('balderas', 1)]
    },
    'bellas_artes': {
        'name': 'Bellas Artes',
        'adjacent': [('salto_del_agua', 1), ('pino_suarez', 2)]
    },
    'morelos': {
        'name': 'Morelos',
        'adjacent': [('san_lazaro', 0), ('candelaria', 0)]
    },
    'balderas': {
        'name': 'Balderas',
        'adjacent': [('salto_del_agua', 0), ('centro_medico', 2), ('tacubaya', 5)]
    },
    'salto_del_agua': {
        'name': 'Salto del Agua',
        'adjacent': [('pino_suarez', 1), ('chabacano', 2)]
    },
    'pino_suarez': {
        'name': 'Pino Suarez',
        'adjacent': [('candelaria', 0), ('chabacano', 1)]
    },
    'san_lazaro': {
        'name': 'San Lázaro',
        'adjacent': [('candelaria', 0), ('pantitlan', 5)]
    },
    'candelaria': {
        'name': 'Candelaria',
        'adjacent': [('jamaica', 1)]
    },
    'tacubaya': {
        'name': 'Tacubaya',
        'adjacent': [('centro_medico', 2), ('mixcoac', 2)]
    },
    'centro_medico': {
        'name': 'Centro Médico',
        'adjacent': [('chabacano', 1), ('zapata', 3)]
    },
    'chabacano': {
        'name': 'Chabacano',
        'adjacent': [('jamaica', 0), ('santa_anita', 1), ('ermita', 5)]
    },
    'jamaica': {
        'name': 'Jamaica',
        'adjacent': [('santa_anita', 0), ('pantitlan', 4)]
    },
    'santa_anita': {
        'name': 'Santa Anita',
        'adjacent': [('atlalilco', 5)]
    },
    'mixcoac': {
        'name': 'Mixcoac',
        'adjacent': [('zapata', 2)]
    },
    'zapata': {
        'name': 'Zapata',
        'adjacent': [('ermita', 2)]
    },
    'ermita': {
        'name': 'Ermita',
        'adjacent': [('atlalilco', 1)]
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
                print(f"metro.add_edge({key}, {station[0]}, {station[1]})")


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


metro.add_edge(rosario, instituto_del_petroleo, 5)
metro.add_edge(rosario, tacuba, 3)
metro.add_edge(instituto_del_petroleo, la_raza, 1)
metro.add_edge(instituto_del_petroleo, deportivo_18, 1)
metro.add_edge(deportivo_18, la_raza, 1)
metro.add_edge(deportivo_18, martin_carrera, 1)
metro.add_edge(martin_carrera, consulado, 2)
metro.add_edge(la_raza, guerrero, 1)
metro.add_edge(la_raza, consulado, 2)
metro.add_edge(consulado, morelos, 1)
metro.add_edge(consulado, oceania, 2)
metro.add_edge(tacuba, hidalgo, 6)
metro.add_edge(tacuba, tacubaya, 4)
metro.add_edge(guerrero, garibaldi, 0)
metro.add_edge(guerrero, hidalgo, 0)
metro.add_edge(garibaldi, bellas_artes, 0)
metro.add_edge(garibaldi, morelos, 2)
metro.add_edge(oceania, san_lazaro, 2)
metro.add_edge(oceania, pantitlan, 2)
metro.add_edge(hidalgo, bellas_artes, 0)
metro.add_edge(hidalgo, balderas, 1)
metro.add_edge(bellas_artes, salto_del_agua, 1)
metro.add_edge(bellas_artes, pino_suarez, 2)
metro.add_edge(morelos, san_lazaro, 0)
metro.add_edge(morelos, candelaria, 0)
metro.add_edge(balderas, salto_del_agua, 0)
metro.add_edge(balderas, centro_medico, 2)
metro.add_edge(balderas, tacubaya, 5)
metro.add_edge(salto_del_agua, pino_suarez, 1)
metro.add_edge(salto_del_agua, chabacano, 2)
metro.add_edge(pino_suarez, candelaria, 0)
metro.add_edge(pino_suarez, chabacano, 1)
metro.add_edge(san_lazaro, candelaria, 0)
metro.add_edge(san_lazaro, pantitlan, 5)
metro.add_edge(candelaria, jamaica, 1)
metro.add_edge(tacubaya, centro_medico, 2)
metro.add_edge(tacubaya, mixcoac, 2)
metro.add_edge(centro_medico, chabacano, 1)
metro.add_edge(centro_medico, zapata, 3)
metro.add_edge(chabacano, jamaica, 0)
metro.add_edge(chabacano, santa_anita, 1)
metro.add_edge(chabacano, ermita, 5)
metro.add_edge(jamaica, santa_anita, 0)
metro.add_edge(jamaica, pantitlan, 4)
metro.add_edge(santa_anita, atlalilco, 5)
metro.add_edge(mixcoac, zapata, 2)
metro.add_edge(zapata, ermita, 2)
metro.add_edge(ermita, atlalilco, 1)

metro.find_path('El Rosario', 'Mixcoac')
print(metro.find_path('El Rosario', 'Mixcoac'))
