from collections import deque

def busqueda_anchura(grafo, inicio, final):
    def explorar(nodo, camino, visitado):
        if nodo == final:
            return camino
        visitado.add(nodo)
        vecinos = [vecino for vecino in grafo[nodo] if vecino not in visitado]
        nuevos_caminos = [camino + [vecino] for vecino in vecinos]
        queue.extend(nuevos_caminos)

    visitado = set()
    queue = deque([[inicio]])

    while queue:
        camino_actual = queue.popleft()
        nodo_actual = camino_actual[-1]

        if nodo_actual not in visitado:
            res = explorar(nodo_actual, camino_actual, visitado)
            if res:
                return res

    return None

grafo = {
    'Escuela': ['Parque', 'Restaurant'],
    'Parque': ['Escuela', 'Cine', 'Biblioteca'],
    'Restaurant': ['Escuela', 'Casa'],
    'Cine': ['Parque'],
    'Biblioteca': ['Parque', 'Casa'],
    'Casa': ['Restaurant', 'Biblioteca']
}

nodo_inicio = 'Parque'
nodo_final = 'Casa'

print("El grafo es:")
print(grafo)

res = busqueda_anchura(grafo, nodo_inicio, nodo_final)
if res:
    print(f"Camino encontrado 1: {res}")
else:
    print("No se encontró un camino.")