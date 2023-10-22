import pycosat

# Definición de operadores y acciones
operators = {
    'A': ['A'],
    'B': ['B'],
    'C': ['C'],
    'D': ['A', 'B'],
    'E': ['B', 'C'],
    'F': ['C'],
}

# Definición del estado inicial y objetivo
initial_state = ['A', 'B']
goal_state = ['C']

# Función para traducir un estado a una fórmula SAT
def state_to_formula(state):
    formula = []
    for operator, conditions in operators.items():
        clause = [operator if condition in state else '-' + operator for condition in conditions]
        formula.append(clause)
    return formula

# Función para resolver un problema de planificación con SATPLAN
def satplan(initial, goal, operators):
    formula = []

    # Agregar cláusulas de estado inicial y objetivo
    formula.extend(state_to_formula(initial))
    formula.extend([['-' + operator] for operator in goal])

    # Agregar cláusulas para garantizar que las acciones sean aplicables
    for operator, conditions in operators.items():
        clause = []
        for condition in conditions:
            clause.append('-' + condition if condition not in initial else condition)
        formula.append(clause)

    # Resolver la fórmula SAT
    solution = pycosat.solve(formula)

    if solution is not None:
        plan = [literal for literal in solution if literal in operators.keys()]
        return plan
    else:
        return None

# Resolver el problema de planificación
plan = satplan(initial_state, goal_state, operators)

if plan:
    print("Plan encontrado:")
    print(plan)
else:
    print("No se pudo encontrar un plan.")
