import numpy as np

# Definir los estados ocultos (HMM con 2 estados: "soleado" y "lluvioso")
states = ["soleado", "lluvioso"]
transition_matrix = np.array([
    [0.7, 0.3],  # Probabilidad de quedarse en "soleado" y transitar a "lluvioso"
    [0.4, 0.6]   # Probabilidad de quedarse en "lluvioso" y transitar a "soleado"
])
# Matriz de emisión (probabilidades de observación para cada estado)
emission_matrix = np.array([
    [0.9, 0.1],  # Probabilidad de observar "paraguas" dado que está "soleado" o "lluvioso"
    [0.2, 0.8]   # Probabilidad de observar "paraguas" dado que está "soleado" o "lluvioso"
])
# Secuencia de observaciones (por ejemplo, observaciones de un paraguas)
observations = ["paraguas", "paraguas", "no paraguas"]

initial_probabilities = np.array([0.6, 0.4])  # Probabilidad inicial de estar en "soleado" o "lluvioso"

# Función para realizar la inferencia de estados ocultos usando el algoritmo de Viterbi
def viterbi(observations, states, initial_probabilities, transition_matrix, emission_matrix):
    num_states = len(states)
    num_observations = len(observations)
    
    # Inicializar matrices para la programación dinámica
    V = np.zeros((num_states, num_observations))
    backpointers = np.zeros((num_states, num_observations), dtype=int)
    
    for s in range(num_states):
     V[s, 0] = initial_probabilities[s] * emission_matrix[s, states.index(observations[0])]

    # Rellenar la matriz V iterativamente
    for t in range(1, num_observations):
        for s in range(num_states):
            max_transition_prob = np.max(V[:, t-1] * transition_matrix[:, s])
            V[s, t] = max_transition_prob * emission_matrix[s, states.index(observations[t])]
            backpointers[s, t] = np.argmax(V[:, t-1] * transition_matrix[:, s])
    
    # Reconstruir la secuencia de estados ocultos
    best_path = [np.argmax(V[:, -1])]
    for t in range(num_observations - 1, 0, -1):
        best_path.append(backpointers[best_path[-1], t])
    
    best_path.reverse()
    
    return [states[i] for i in best_path]
hidden_states = viterbi(observations, states, initial_probabilities, transition_matrix, emission_matrix)
print("Secuencia de estados ocultos inferida:", hidden_states)