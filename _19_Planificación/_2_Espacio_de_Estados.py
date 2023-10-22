import queue

class Estado:
    def __init__(self, nodo, costo_acumulado, camino):
        self.nodo = nodo
        self.costo_acumulado = costo_acumulado
        self.camino = camino

    def __lt__(self, other):
        return self.costo_acumulado < other.costo_acumulado

def encontrar_camino_mas_corto(grafo, inicio, objetivo):
    frontera = queue.PriorityQueue()
    frontera.put(Estado(inicio, 0, [inicio]))
    explorado = set()

    while not frontera.empty():
        estado_actual = frontera.get()
        nodo_actual = estado_actual.nodo

        if nodo_actual == objetivo:
            return estado_actual.camino

        if nodo_actual in explorado:
            continue

        explorado.add(nodo_actual)

        for vecino, costo in grafo[nodo_actual].items():
            if vecino not in explorado:
                costo_acumulado = estado_actual.costo_acumulado + costo
                camino = estado_actual.camino + [vecino]
                frontera.put(Estado(vecino, costo_acumulado, camino))

    return None

# Ejemplo de un grafo representado como un diccionario de diccionarios
grafo = {
    'A': {'B': 1, 'C': 3},
    'B': {'A': 1, 'D': 2},
    'C': {'A': 3, 'D': 1},
    'D': {'B': 2, 'C': 1, 'E': 4},
    'E': {'D': 4}
}

inicio = 'A'
objetivo = 'E'

camino = encontrar_camino_mas_corto(grafo, inicio, objetivo)

if camino is not None:
    print(f"Camino más corto desde {inicio} a {objetivo}: {camino}")
else:
    print(f"No se encontró un camino desde {inicio} a {objetivo}.")
