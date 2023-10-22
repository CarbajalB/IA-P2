import random

def calcular_conflictos(tablero):
    n = len(tablero)
    conflictos = 0
    for i in range(n):
        for j in range(i + 1, n):
            if tablero[i] == tablero[j] or abs(tablero[i] - tablero[j]) == j - i:
                conflictos += 1
    return conflictos

def encontrar_minimos_conflictos(n, max_iter):
    tablero = [random.randint(0, n-1) for _ in range(n)]
    for _ in range(max_iter):
        conflictos = calcular_conflictos(tablero)
        if conflictos == 0:
            return tablero
        
        conflicto_min = float('inf')
        mejores_movimientos = []
        for col in range(n):
            actual = tablero[col]
            for fila in range(n):
                if fila != actual:
                    tablero[col] = fila
                    nuevos_conflictos = calcular_conflictos(tablero)
                    if nuevos_conflictos < conflicto_min:
                        mejores_movimientos = [fila]
                        conflicto_min = nuevos_conflictos
                    elif nuevos_conflictos == conflicto_min:
                        mejores_movimientos.append(fila)
            
            tablero[col] = random.choice(mejores_movimientos)
    return None
n = 8  
max_iter = 1000  
solucion = encontrar_minimos_conflictos(n, max_iter)
if solucion is not None:
    print("Solucion encontrada:", solucion)
else:
    print("No se encontro solucion en el numero maximo de iteraciones")
