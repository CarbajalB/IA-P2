def busqueda_en_profundidad_limitada(grafo, nodo_actual, visitados, profundidad_maxima):
    if profundidad_maxima == 0: 
        return
    if nodo_actual not in visitados: 
        print(nodo_actual) 
        visitados.add(nodo_actual)
        for vecino in grafo[nodo_actual]: 
            busqueda_en_profundidad_limitada(grafo, vecino, visitados, profundidad_maxima - 1) 
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
}
nodo_inicial = 'D'
visitados = set()  
profundidad_maxima = 4 
print(f"Recorrido en profundidad limitada (profundidad maxima: {profundidad_maxima}) del grafo:")
busqueda_en_profundidad_limitada(grafo, nodo_inicial, visitados, profundidad_maxima)