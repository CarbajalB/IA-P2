import numpy as np
from scipy.optimize import minimize

# Definición del problema
num_agents = 2
initial_positions = np.array([[0.0, 0.0], [1.0, 1.0]])
destinations = np.array([[3.0, 3.0], [2.0, 2.0]])

# Función de costo para la optimización (distancia Euclidiana)
def cost_function(positions, destinations):
    return np.sum(np.linalg.norm(positions - destinations, axis=1))

# Función de restricción para evitar colisiones entre agentes
def collision_constraint(positions):
    return np.linalg.norm(positions[0] - positions[1]) - 0.5  # Evitar colisiones a menos de 0.5 unidades

# Optimización de las rutas para cada agente
routes = []
for agent in range(num_agents):
    result = minimize(cost_function, initial_positions[agent], args=(destinations[agent],),
                      constraints={'type': 'ineq', 'fun': collision_constraint})
    routes.append(result.x)

# Imprimir las rutas encontradas
for agent, route in enumerate(routes):
    print(f"Agente {agent + 1}: Ruta óptima = {route}, Costo = {result.fun:.2f}")
