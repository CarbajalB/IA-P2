import numpy as np

# Definir el problema del bandit
num_bandits = 100
true_action_values = np.random.normal(0, 1, num_bandits)

# Función para seleccionar una acción basada en una política epsilon-greedy
def select_action(Q, epsilon):
    if np.random.rand() < epsilon:
        # Exploración: elige una acción aleatoria
        return np.random.choice(len(Q))
    else:
        # Explotación: elige la acción con el valor estimado máximo
        return np.argmax(Q)

# Algoritmo de Monte Carlo para búsqueda de política
num_episodes = 1000
epsilon = 0.1
Q = np.zeros(num_bandits)  # Valores estimados de las acciones

for episode in range(num_episodes):
    action = select_action(Q, epsilon)
    reward = np.random.normal(true_action_values[action], 1)
    Q[action] = Q[action] + (reward - Q[action]) / (episode + 1)

# Imprimir la política aprendida
best_action = np.argmax(Q)
print("Política óptima (acción con el valor estimado máximo):", best_action)
