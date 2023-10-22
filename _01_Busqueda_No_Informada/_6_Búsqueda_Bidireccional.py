def busqueda_bidireccional(grafo, nodo_inicial, nodo_objetivo):
    conjunto_inicio = set([nodo_inicial])
    conjunto_objetivo = set([nodo_objetivo])
    while conjunto_inicio and conjunto_objetivo:
        interseccion = conjunto_inicio & conjunto_objetivo
        if interseccion:
            return list(interseccion)

        conjunto_inicio = {vecino for nodo in conjunto_inicio for vecino in grafo.get(nodo, [])}
        conjunto_objetivo = {vecino for nodo in conjunto_objetivo for vecino in grafo.get(nodo, [])}
    return None
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B', 'E'],
    'E': ['C', 'D', 'F'],
    'F': ['E']
}
nodo_inicial = 'E'
nodo_objetivo = 'A'
camino = busqueda_bidireccional(grafo, nodo_inicial, nodo_objetivo)
if camino:
    print("Camino encontrado:", " -> ".join(camino))
else:
    print("No se encontro un camino.")