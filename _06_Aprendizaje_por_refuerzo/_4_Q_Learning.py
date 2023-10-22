import numpy as np

# Definir el entorno de cuadrícula
# 'S' representa el estado inicial, 'G' es el estado objetivo, 'F' es un espacio libre, y 'H' es un obstáculo
grid = [
    ['S', 'F', 'F', 'F'],
    ['F', 'H', 'F', 'H'],
    ['F', 'F', 'F', 'H'],
    ['H', 'F', 'F', 'G']
]

# Definir los parámetros de Q-Learning
num_states = 16
num_actions = 4
Q = np.zeros((num_states, num_actions))  # Tabla Q inicializada a cero
gamma = 0.9  # Factor de descuento
alpha = 0.1  # Tasa de aprendizaje

# Función para mapear las coordenadas (x, y) a un estado único
def state_from_coords(x, y):
    return y * 4 + x

# Función para mapear un estado único a coordenadas (x, y)
def coords_from_state(state):
    y, x = divmod(state, 4)
    return x, y

# Función para seleccionar una acción basada en ε-greedy
def select_action(state, epsilon):
    if np.random.rand() < epsilon:
        return np.random.choice(num_actions)  # Exploración aleatoria
    else:
        return np.argmax(Q[state, :])  # Explotación de la política

# Bucle de entrenamiento
num_episodes = 1000

for _ in range(num_episodes):
    state = state_from_coords(0, 0)  # Comenzar desde el estado inicial
    done = False

    while not done:
        epsilon = 0.1  # Probabilidad de exploración (ε)
        action = select_action(state, epsilon)  # Seleccionar una acción
        x, y = coords_from_state(state)

        if action == 0:  # Arriba
            new_x, new_y = x, y - 1
        elif action == 1:  # Abajo
            new_x, new_y = x, y + 1
        elif action == 2:  # Izquierda
            new_x, new_y = x - 1, y
        else:  # Derecha
            new_x, new_y = x + 1, y

        new_x = max(0, min(new_x, 3))
        new_y = max(0, min(new_y, 3))
        new_state = state_from_coords(new_x, new_y)

        # Definir recompensas
        if grid[new_y][new_x] == 'H':
            reward = -1  # Recompensa negativa por chocar con un obstáculo
        elif grid[new_y][new_x] == 'G':
            reward = 1  # Recompensa positiva por llegar al objetivo
            done = True
        else:
            reward = 0  # Recompensa cero por moverse a un espacio libre

        # Actualizar la tabla Q
        Q[state, action] = Q[state, action] + alpha * (reward + gamma * np.max(Q[new_state, :]) - Q[state, action])
        state = new_state

# Evaluar la política aprendida
state = state_from_coords(0, 0)
path = [(0, 0)]

while state != state_from_coords(3, 3):
    action = select_action(state, epsilon=0)  # Explotar la política aprendida
    x, y = coords_from_state(state)

    if action == 0:  # Arriba
        new_x, new_y = x, y - 1
    elif action == 1:  # Abajo
        new_x, new_y = x, y + 1
    elif action == 2:  # Izquierda
        new_x, new_y = x - 1, y
    else:  # Derecha
        new_x, new_y = x + 1, y

    new_x = max(0, min(new_x, 3))
    new_y = max(0, min(new_y, 3))
    new_state = state_from_coords(new_x, new_y)
    state = new_state
    path.append((new_x, new_y))

print("Camino óptimo:")
for x, y in path:
    print(f'({x}, {y})')
