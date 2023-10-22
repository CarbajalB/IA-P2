import pyhop

# Definición de funciones de operador
def move(state, robot, source, destination):
    if state.holding[robot] == source and state.clear[destination]:
        state.holding[robot] = None
        state.clear[source] = True
        state.clear[destination] = False
        state.on[source] = None
        state.on[destination] = source
        return state
    else:
        return False

def pickup(state, robot, block):
    if state.clear[block] and not state.holding[robot]:
        state.holding[robot] = block
        state.clear[block] = False
        state.on[block] = None
        return state
    else:
        return False

def putdown(state, robot, block):
    if state.holding[robot] == block:
        state.holding[robot] = None
        state.clear[block] = True
        state.on[block] = None
        return state
    else:
        return False

# Definición de metas
def move_to_goal(state, robot, source, destination):
    return [('move', robot, source, destination)]

def stack_blocks(state, robot, block1, block2):
    return [('pickup', robot, block1), ('move', robot, block1, block2), ('putdown', robot, block2)]

# Crear un estado inicial
initial_state = pyhop.State('initial_state')
initial_state.holding = {'robot': None}
initial_state.clear = {'A': True, 'B': True, 'C': True}
initial_state.on = {'A': None, 'B': None, 'C': None}

# Crear un problema y resolverlo
pyhop.declare_operators(move, pickup, putdown)
pyhop.declare_methods('move_to_goal', move_to_goal)
pyhop.declare_methods('stack_blocks', stack_blocks)

goal_state = move_to_goal(initial_state, 'robot', 'A', 'C')
solution = pyhop.pyhop(initial_state, goal_state, verbose=1)

if solution is not None:
    print("Plan encontrado:")
    for step in solution:
        print(step)
else:
    print("No se pudo encontrar un plan.")
