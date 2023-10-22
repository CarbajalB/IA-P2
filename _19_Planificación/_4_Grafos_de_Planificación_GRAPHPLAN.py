class GraphPlanNode:
    def __init__(self, level):
        self.level = level
        self.mutexes = set()
        self.actions = set()

def is_mutex(action1, action2, prev_level, state_mutexes):
    # Verificar si dos acciones son mutuamente excluyentes
    if (action1, action2) in prev_level.mutexes:
        return True

    for pair in state_mutexes:
        if all(elem in prev_level.actions for elem in pair):
            return True

    return False

def graphplan(problem):
    initial = problem['initial']
    goals = problem['goals']
    actions = problem['actions']

    # Inicializar el primer nivel
    level = 0
    nodes = [GraphPlanNode(level)]
    nodes[level].actions.update(initial)

    while level < 2 * len(actions):  # Se limita el número de niveles para simplificar
        prev_level = nodes[level]
        level += 1
        nodes.append(GraphPlanNode(level))

        # Agregar acciones que son aplicables en el nivel actual
        for action in actions:
            if action.preconditions.issubset(prev_level.actions):
                nodes[level].actions.add(action)

        # Agregar literales que no son negativos en el nivel actual
        state_mutexes = set()
        for literal in initial:
            if literal not in goals and literal not in prev_level.mutexes:
                nodes[level].actions.add(f"ACHIEVE_{literal}")
                state_mutexes.add(frozenset((literal, f"ACHIEVE_{literal}")))

        # Agregar literales que son negativos en el nivel actual
        for literal in goals:
            if literal not in prev_level.mutexes:
                nodes[level].actions.add(f"ACHIEVE_NOT_{literal}")
                state_mutexes.add(frozenset((literal, f"ACHIEVE_NOT_{literal}")))

        # Verificar mutexes entre acciones en el nivel actual
        for action1 in nodes[level].actions:
            for action2 in nodes[level].actions:
                if action1 != action2 and is_mutex(action1, action2, prev_level, state_mutexes):
                    nodes[level].mutexes.add(frozenset((action1, action2)))

        # Si todos los objetivos están presentes en el nivel actual, la planificación es exitosa
        if goals.issubset(nodes[level].actions):
            return extract_plan(nodes, goals, actions)

    return None

def extract_plan(nodes, goals, actions):
    plan = []
    for level in reversed(range(len(nodes) - 1)):
        node = nodes[level]
        achieved_goals = goals.intersection(node.actions)
        if achieved_goals:
            # Encontrar una acción que logra uno de los objetivos y agregarla al plan
            for action in actions:
                if action.effects.intersection(achieved_goals):
                    plan.append(action)
                    goals.remove(achieved_goals.pop())
                    break
    return plan

class Action:
    def __init__(self, name, preconditions, effects):
        self.name = name
        self.preconditions = preconditions
        self.effects = effects

if __name__ == "__main__":
    # Definir el problema de planificación
    initial_state = {"A", "B"}
    goal_state = {"C"}
    actions = [
        Action("Action1", {"A"}, {"B"}),
        Action("Action2", {"B"}, {"C"}),
        Action("Action3", set(), {"A"}),
    ]

    problem = {
        'initial': initial_state,
        'goals': goal_state,
        'actions': actions
    }

    # Resolver el problema utilizando GRAPHPLAN
    plan = graphplan(problem)

    if plan:
        print("Plan encontrado:")
        for action in plan:
            print(action.name)
    else:
        print("No se pudo encontrar un plan.")
