
def busqueda_prof(grafo,inicio,final):
    def explorar(nodo,camino, visitado):
        if nodo == final:
            return camino
        visitado.add(nodo)
        vecinos=[vecino for vecino in grafo[nodo] if vecino not in visitado]
        for vecino in vecinos:
            res=explorar(vecino,camino + [vecino], visitado)
            if res:
                return res
    visitado=set()
    return explorar(inicio, [inicio], visitado)
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

res2= busqueda_prof(grafo,nodo_inicio,nodo_final)
if res2:
    print(f"Camino encontrado 2: {res2}")
else:
    print("No se encontró un camino.")