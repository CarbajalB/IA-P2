import numpy as np
import random

# Definir el entorno (en este caso, un mundo de cuadrícula simple)
# 0: espacio libre
# 1: obstáculo
# 2: objetivo
world = np.array([
    [0, 0, 0, 1],
    [0, 1, 0, 1],
    [0, 1, 0, 1],
    [0, 0, 0, 2]
])

# Definir los parámetros del aprendizaje por refuerzo activo
gamma = 0.9  # Factor de descuento
learning_rate = 0.1

# Inicializar la tabla Q con valores arbitrarios
num_states = np.prod(world.shape)
num_actions = 4  # 4 posibles acciones: arriba, abajo, izquierda, derecha
Q = np.zeros((num_states, num_actions))

# Función para convertir coordenadas (x, y) a un estado único
def state_from_coords(x, y):
    return x + y * world.shape[1]

# Función para convertir un estado único a coordenadas (x, y)
def coords_from_state(state):
    y, x = divmod(state, world.shape[1])
    return x, y

# Función para seleccionar una acción basada en ε-greedy
def select_action(state, epsilon):
    if random.uniform(0, 1) < epsilon:
        return random.choice(range(num_actions))  # Exploración aleatoria
    else:
        return np.argmax(Q[state, :])  # Explotación de la política

# Entrenar al agente mediante Q-learning
num_episodes = 1000

for _ in range(num_episodes):
    state = state_from_coords(0, 0)
    done = False

    while not done:
        epsilon = 0.1  # Probabilidad de exploración (ε)
        action = select_action(state, epsilon)
        x, y = coords_from_state(state)

        if action == 0:  # Arriba
            new_x, new_y = x, y - 1
        elif action == 1:  # Abajo
            new_x, new_y = x, y + 1
        elif action == 2:  # Izquierda
            new_x, new_y = x - 1, y
        else:  # Derecha
            new_x, new_y = x + 1, y

        if 0 <= new_x < world.shape[1] and 0 <= new_y < world.shape[0] and world[new_y, new_x] != 1:
            new_state = state_from_coords(new_x, new_y)
            reward = -1  # Recompensa por movimiento
        else:
            new_state = state
            reward = -5  # Recompensa por chocar con un obstáculo

        Q[state, action] += learning_rate * (reward + gamma * np.max(Q[new_state, :]) - Q[state, action])
        state = new_state

        if world[coords_from_state(state)] == 2:
            done = True  # El agente llegó al objetivo

# Probar la política aprendida
state = state_from_coords(0, 0)
done = False
steps = 0

while not done:
    action = select_action(state, 0)  # Explotación completa
    x, y = coords_from_state(state)

    if action == 0:
        new_x, new_y = x, y - 1
    elif action == 1:
        new_x, new_y = x, y + 1
    elif action == 2:
        new_x, new_y = x - 1, y
    else:
        new_x, new_y = x + 1, y

    if 0 <= new_x < world.shape[1] and 0 <= new_y < world.shape[0] and world[new_y, new_x] != 1:
        state = state_from_coords(new_x, new_y)
        steps += 1

        if world[coords_from_state(state)] == 2:
            done = True

print(f"El agente llegó al objetivo en {steps} pasos.")
