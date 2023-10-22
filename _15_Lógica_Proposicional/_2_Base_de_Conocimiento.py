# Definir una base de conocimiento de animales y sus características
base_de_conocimiento = {
    'perro': {
        'tipo': 'mamífero',
        'patas': 4,
        'cola': True
    },
    'gato': {
        'tipo': 'mamífero',
        'patas': 4,
        'cola': True
    },
    'pájaro': {
        'tipo': 'ave',
        'patas': 2,
        'cola': True
    },
    'serpiente': {
        'tipo': 'reptil',
        'patas': 0,
        'cola': True
    }
}

# Consultar la base de conocimiento
animal = 'perro'
if animal in base_de_conocimiento:
    caracteristicas = base_de_conocimiento[animal]
    print(f"El {animal} es un {caracteristicas['tipo']} con {caracteristicas['patas']} patas y cola: {caracteristicas['cola']}")
else:
    print(f"No se encontró información sobre el {animal}")

# Resultado esperado:
# El perro es un mamífero con 4 patas y cola: True
