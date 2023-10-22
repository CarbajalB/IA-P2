def Busqueda_iterativa(grafo, nodo_inicial, nodo_objetivo):
    profundidad_maxima = 0 
    while True: 
        visitados = set()
        resultado =  Busqueda_limitada(grafo, nodo_inicial, nodo_objetivo, profundidad_maxima, visitados)
        if resultado is not None: 
            return resultado
        profundidad_maxima += 1
#Se realiza una busqueda maxima 
def Busqueda_limitada(grafo, nodo, objetivo, profundidad_maxima, visitados):
    if profundidad_maxima == 0 and nodo == objetivo:
        return [nodo]
    elif profundidad_maxima > 0:
        visitados.add(nodo)
        for vecino in grafo[nodo]:
            if vecino not in visitados:
                camino = Busqueda_limitada(grafo, vecino, objetivo, profundidad_maxima - 1, visitados)
                if camino is not None:
                    return [nodo] + camino
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
}
nodo_inicial = 'B'
nodo_objetivo = 'E'
resultado = Busqueda_iterativa(grafo, nodo_inicial, nodo_objetivo)
if resultado:
    print("Camino encontrado:", " , ".join(resultado))
else:
    print("No se encontro un camino.")