import numpy as np

# Definir el entorno (laberinto) como una matriz
# 0: espacio libre
# 1: obstáculo
# 2: objetivo
laberinto = np.array([
    [0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 2]
])

# Definir los ejemplos de estados, acciones y recompensas
ejemplos = [
    ((0, 0), 1, -1),
    ((0, 1), 1, -1),
    ((1, 1), 0, -1),
    ((2, 1), 0, -1),
    ((2, 0), 3, -1),
    ((3, 0), 3, -1),
    ((4, 0), 3, -1),
    ((4, 1), 0, -1),
    ((4, 2), 1, -1),
    ((3, 2), 1, -1),
    ((3, 3), 2, 10)  # Objetivo
]

# Inicializar la política de toma de decisiones
politica = np.zeros_like(laberinto)

# Aprender la política desde los ejemplos
for estado, accion, recompensa in ejemplos:
    politica[estado] = accion
print("Política de toma de decisiones:")
print(politica)
