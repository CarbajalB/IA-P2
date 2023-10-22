def es_seguro(tablero, fila, columna, n):
    # Verificar si una reina puede ser colocada en la posición (fila, columna)
    # Verificar la misma columna
    for i in range(fila):
        if tablero[i][columna] == 1:
            return False

    # Verificar la diagonal izquierda superior
    for i, j in zip(range(fila, -1, -1), range(columna, -1, -1)):
        if tablero[i][j] == 1:
            return False

    # Verificar la diagonal derecha superior
    for i, j in zip(range(fila, -1, -1), range(columna, n)):
        if tablero[i][j] == 1:
            return False

    return True

def resolver_n_reinas(n):
    tablero = [[0 for _ in range(n)] for _ in range(n)]
    
    def resolver(fila):
        if fila == n:
            # Todas las reinas han sido colocadas con éxito
            return True
        for columna in range(n):
            if es_seguro(tablero, fila, columna, n):
                tablero[fila][columna] = 1
                if resolver(fila + 1):
                    return True
                tablero[fila][columna] = 0

        return False

    if not resolver(0):
        print("No se encontró una solución.")
    else:
        for fila in tablero:
            print(fila)

# Resolver el problema de las 8 reinas
resolver_n_reinas(8)
