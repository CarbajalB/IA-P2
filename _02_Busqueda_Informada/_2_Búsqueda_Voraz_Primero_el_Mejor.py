from queue import PriorityQueue
mapa = {
    'Casa': [('Parque', 5), ('Tienda', 3)],  
    'Parque': [('Biblioteca', 10)],
    'Tienda': [('Biblioteca', 5)],
    'Biblioteca': []
}
def voraz_primero_el_mejor(mapa, inicio, destino): 
    frontera = PriorityQueue()
    frontera.put((0, inicio)) 
    visitados = set()

    while not frontera.empty():
        costo, ubicacion_actual = frontera.get()

        if ubicacion_actual == destino:
            print("Has llegado a la Escuela desde tu Casa:", costo, "minutos")
            break

        if ubicacion_actual not in visitados:
            visitados.add(ubicacion_actual)

            for vecino, tiempo_viaje in mapa[ubicacion_actual]:
                if vecino not in visitados:
                    frontera.put((tiempo_viaje, vecino))
inicio = 'Casa'
destino = 'Biblioteca'
voraz_primero_el_mejor(mapa, inicio, destino)