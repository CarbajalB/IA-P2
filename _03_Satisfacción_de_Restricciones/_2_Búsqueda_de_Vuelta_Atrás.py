class CSP:
    def __init__(self):
        self.variables = ["A", "B", "C"]
        self.domains = {
            "A": [1, 2, 3],
            "B": [1, 2, 3],
            "C": [1, 2, 3]
        }
        self.neighbors = {
            "A": ["B", "C"],
            "B": ["A", "C"],
            "C": ["A", "B"]
        }
def select_unassigned_variable(assignment, csp):
    for var in csp.variables:
        if var not in assignment:
            return var
    return None
def order_domain_values(var, assignment, csp):
    return csp.domains[var]
def is_consistent(var, value, assignment, csp):
    for neighbor in csp.neighbors[var]:
        if neighbor in assignment and assignment[neighbor] == value:
            return False
    return True
def forward_checking(csp):
    return recursive_forward_checking({}, csp)

def recursive_forward_checking(assignment, csp):
    if len(assignment) == len(csp.variables):
        return assignment

    var = select_unassigned_variable(assignment, csp)
    for value in order_domain_values(var, assignment, csp):
        if is_consistent(var, value, assignment, csp):
            assignment[var] = value
            pruned_domains = forward_check(var, value, assignment, csp)
            if pruned_domains is not None:
                result = recursive_forward_checking(assignment, csp)
                if result is not None:
                    return result
                undo_forward_check(var, value, assignment, pruned_domains, csp)
            del assignment[var]
    return None

def forward_check(var, value, assignment, csp):
    pruned_domains = {}
    for neighbor in csp.neighbors[var]:
        if neighbor not in assignment:
            pruned_values = []
            for neighbor_value in csp.domains[neighbor]:
                if not is_consistent(neighbor, neighbor_value, assignment, csp):
                    pruned_values.append(neighbor_value)
            if pruned_values == csp.domains[neighbor]:
                return None
            pruned_domains[neighbor] = pruned_values
            csp.domains[neighbor] = [v for v in csp.domains[neighbor] if v not in pruned_values]
    return pruned_domains

def undo_forward_check(var, value, assignment, pruned_domains, csp):
    for neighbor, pruned_values in pruned_domains.items():
        csp.domains[neighbor].extend(pruned_values)
problem = CSP() 
solution = forward_checking(problem)
print("Solucion encontrada:", solution)

