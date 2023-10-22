from htnpy import Task, Method, htn

# Definición de tareas
@Task
def make_breakfast(state):
    if state["got up"] and not state["breakfast"]:
        state["breakfast"] = True

@Task
def get_up(state):
    if not state["got up"]:
        state["got up"] = True

# Definición de métodos
@Method
def wake_up(state):
    return [("get_up", )]

@Method
def eat_breakfast(state):
    return [("get_up", ), ("make_breakfast", )]

# Definir el planificador HTN
planner = htn()

# Estado inicial
initial_state = {"got up": False, "breakfast": False}

# Planificación
goal = [("eat_breakfast", )]
plan = planner(initial_state, goal)

if plan:
    print("Plan encontrado:")
    for task in plan:
        print(task)
else:
    print("No se pudo encontrar un plan.")
