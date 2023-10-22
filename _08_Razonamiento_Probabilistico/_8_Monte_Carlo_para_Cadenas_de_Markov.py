import random

# Transiciones de la cadena de Markov
transitions = {
    'A': {'A': 0.7, 'B': 0.3},
    'B': {'A': 0.4, 'B': 0.6}
}

current_state = 'A'
num_iterations = 10000
state_counts = {'A': 0, 'B': 0}

# Realiza el muestreo de Monte Carlo para cadenas de Markov
for _ in range(num_iterations):
    # Realiza una transicion segun las probabilidades de transicion
    next_state = random.choices(list(transitions[current_state].keys()), 
                                weights=list(transitions[current_state].values()))[0]
    # Actualiza el estado actual
    current_state = next_state
    # Registra el estado actual
    state_counts[current_state] += 1
# Calcula las probabilidades estimadas de estar en cada estado
estimated_probabilities = {state: count / num_iterations for state, count in state_counts.items()}
print("Probabilidad de estar en el estado 'A':", estimated_probabilities['A'])
print("Probabilidad de estar en el estado 'B':", estimated_probabilities['B'])