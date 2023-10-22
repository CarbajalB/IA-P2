import heapq

ruta_desde_hasta = {
    "Casa": {"Calle A": 2, "Calle B": 3}, 
    "Calle A": {"Cine": 5},
    "Calle B": {"Cine": 4},
    "Cine": {},
}

def encontrar_ruta(grafo, ubicacion_inicio, ubicacion_destino):
    abierto = [(0, ubicacion_inicio)] 
    antecesores = {} 
    costo_g = {ubicacion: float('inf') for ubicacion in grafo} 
    costo_g[ubicacion_inicio] = 0
    while abierto: 
        costo_actual, ubicacion_actual = heapq.heappop(abierto)

        if ubicacion_actual == ubicacion_destino: 
            ruta = reconstruir_ruta(antecesores, ubicacion_actual)
            return ruta
        for vecino, distancia in grafo[ubicacion_actual].items():
            costo_tentativo_g = costo_g[ubicacion_actual] + distancia
            if costo_tentativo_g < costo_g[vecino]:
                antecesores[vecino] = ubicacion_actual
                costo_g[vecino] = costo_tentativo_g
                costo_f = costo_tentativo_g + heuristica(vecino, ubicacion_destino)
                heapq.heappush(abierto, (costo_f, vecino))
    return None
def heuristica(ubicacion, destino):   
    return 0
def reconstruir_ruta(antecesores, ubicacion_actual):
    ruta = [ubicacion_actual]
    while ubicacion_actual in antecesores:
        ubicacion_actual = antecesores[ubicacion_actual]
        ruta.insert(0, ubicacion_actual)
    return ruta
ubicacion_inicio = "Casa"
ubicacion_destino = "Cine"

ruta_optima = encontrar_ruta(ruta_desde_hasta, ubicacion_inicio, ubicacion_destino)
print("Ruta mas corta:", ruta_optima)