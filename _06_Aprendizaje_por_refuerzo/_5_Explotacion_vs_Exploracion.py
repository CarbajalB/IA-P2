import random

# Recompensas estimadas para cada acción (valores hipotéticos)
Q_values = [1.0, 2.0, 3.0, 4.0, 5.0]

# Función para seleccionar una acción basada en ε-greedy
def epsilon_greedy(epsilon):
    if random.uniform(0, 1) < epsilon:
        # Exploración: elige una acción al azar con probabilidad ε
        return random.choice(range(len(Q_values)))
    else:
        # Explotación: elige la acción con el valor Q máximo
        return Q_values.index(max(Q_values))

# Probabilidad de exploración (ε)
epsilon = 0.2

# Realizar 100 selecciones de acciones utilizando ε-greedy
for _ in range(100):
    action = epsilon_greedy(epsilon)
    print(f"Acción seleccionada: {action}")

# Resultados esperados:
# Las acciones seleccionadas variarán entre la explotación de la mejor acción y la exploración aleatoria con probabilidad ε.
