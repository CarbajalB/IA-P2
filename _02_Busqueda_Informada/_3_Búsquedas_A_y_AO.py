import heapq

grafo = {
    'Escuela': {'Parque': 20, 'Tienda': 10},
    'Parque': {'Casa': 15},
    'Tienda': {'Casa': 5, 'Cine': 5},
    'Casa': {},
    'Cine': {}
}

def buscar_ruta_A_estrella(grafo, inicio, objetivo):
    frontera = [(0, inicio)]  
    visitados = set()  

    while frontera:
        costo, nodo_actual = heapq.heappop(frontera)

        if nodo_actual == objetivo:
            return costo  

        if nodo_actual in visitados:
            continue

        visitados.add(nodo_actual)

        for vecino, costo_camino in grafo[nodo_actual].items():
            if vecino not in visitados:
                costo_total = costo + costo_camino
                heapq.heappush(frontera, (costo_total, vecino))

    return None 
inicio = 'Escuela'
objetivo = 'Cine'
tiempo = buscar_ruta_A_estrella(grafo, inicio, objetivo)
if tiempo is not None:
    print(f"La ruta mas corta desde {inicio} hasta {objetivo} y tardas {tiempo} minutos.")
else:
    print(f"No se encontro una ruta desde {inicio} hasta {objetivo}.")
