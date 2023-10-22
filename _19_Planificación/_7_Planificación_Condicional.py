import pyhop

# Definición de acciones con condiciones
def move(state, agent, location1, location2):
    if state.holding[agent] is None and state.at[agent] == location1:
        state.at[agent] = location2
        return state
    else:
        return False

def pickup(state, agent, object, location):
    if state.at[agent] == location and state.holding[agent] is None and state.clear[object]:
        state.holding[agent] = object
        state.clear[object] = False
        return state
    else:
        return False

def putdown(state, agent, object, location):
    if state.holding[agent] == object and state.at[agent] == location:
        state.holding[agent] = None
        state.clear[object] = True
        return state
    else:
        return False

# Creación de un estado inicial
initial_state = pyhop.State('initial_state')
initial_state.at = {'agent': 'A', 'box': 'B'}
initial_state.holding = {'agent': None}
initial_state.clear = {'A': True, 'B': False}

# Creación de una meta
goal_state = pyhop.State('goal_state')
goal_state.at = {'agent': 'A', 'box': 'B'}
goal_state.holding = {'agent': None}
goal_state.clear = {'A': True, 'B': True}

# Agregar las acciones al planificador
pyhop.declare_operators(move, pickup, putdown)

# Resolver el problema de planificación
solution = pyhop.pyhop(initial_state, [('move', 'agent', 'A', 'B')], verbose=1)

if solution is not None:
    print("Plan encontrado:")
    for step in solution:
        print(step)
else:
    print("No se pudo encontrar un plan.")
