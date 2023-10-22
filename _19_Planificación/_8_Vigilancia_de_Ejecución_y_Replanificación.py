import pyhop

# Definición de acciones
def move_to(state, agent, goal):
    if state['at'][agent] != goal:
        return [('move', agent, goal)]
    return []

def move(agent, goal):
    return f"Mover {agent} a {goal}"

# Función para simular el ambiente
def simulate_environment(agent, goal):
    if agent == 'A' and goal == 'B':
        return True
    return False

# Función de monitoreo
def monitor(agent, goal):
    if not simulate_environment(agent, goal):
        print(f"¡Alerta! La posición de {agent} y el objetivo {goal} no coinciden.")
        return True
    return False

# Función de replanificación
def replan(agent, goal):
    print(f"Replanificando para mover {agent} a {goal}...")
    return [('move', agent, goal)]

# Creación de un estado inicial
initial_state = pyhop.State('initial_state')
initial_state['at'] = {'A': 'A'}

# Definición del problema y objetivo
problem = ('mueve_a_B', [('move_to', 'A', 'B')])

# Planificación inicial
plan = pyhop.pyhop(initial_state, problem, verbose=1)

if plan is not None:
    print("Plan inicial encontrado:")
    for action in plan:
        agent, goal = action[1], action[2]
        if monitor(agent, goal):
            new_plan = pyhop.pyhop(initial_state, ('replan', [(agent, goal)]), verbose=1)
            if new_plan:
                print("Nuevo plan encontrado:")
                for new_action in new_plan:
                    print(move(new_action[1], new_action[2]))
            else:
                print("No se pudo encontrar un nuevo plan.")
        else:
            print(move(agent, goal))
else:
    print("No se pudo encontrar un plan inicial.")
