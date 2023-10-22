import heapq

def distancia_recorrida(busqueda_grafo, nodo_inicial, nodo_objetivo): #creamos una funcion que contiene 3 parametros 
    
    cola = [(0, nodo_inicial)]
    visitados = set()  # Conjunto de nodos visitados

    while cola:
        costo_actual, nodo_actual = heapq.heappop(cola)  # Extraer el nodo con menor costo
        if nodo_actual in visitados:
            continue  

        visitados.add(nodo_actual)

        if nodo_actual == nodo_objetivo:
            return costo_actual  # Hemos encontrado el nodo objetivo

        # Expandir el nodo actual y agregar los sucesores a la cola de prioridad
        for vecino, costo in busqueda_grafo[nodo_actual].items():
            if vecino not in visitados:
                nuevo_costo = costo_actual + costo
                heapq.heappush(cola, (nuevo_costo, vecino))

    return float("inf")  
grafo = {
    'Mi_casa': {'Tienda': 1, 'Papeleria': 4},
    'Tienda': {'Mi_casa': 1, 'OXXO': 2},
    'Papeleria': {'Mi_casa': 4, 'OXXO': 5},
    'OXXO': {'Tienda': 2, 'Papeleria': 5, 'Escuela': 3},
    'Escuela': {'OXXO': 3}
}

nodo_inicial = 'Mi_casa'
nodo_objetivo = 'Escuela'

distancia = distancia_recorrida(grafo, nodo_inicial, nodo_objetivo)

if distancia != float("inf"):
    print(f"La distancia desde {nodo_inicial} a la {nodo_objetivo} es {distancia} kilometros")
else:
    print(f"No se encontro una ruta desde {nodo_inicial} a {nodo_objetivo}")