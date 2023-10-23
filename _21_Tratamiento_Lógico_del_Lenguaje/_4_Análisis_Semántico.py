class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def declare_variable(self, name, data_type):
        if name in self.symbols:
            raise Exception(f"Error semántico: Variable '{name}' ya declarada.")
        self.symbols[name] = data_type

    def check_variable(self, name):
        if name not in self.symbols:
            raise Exception(f"Error semántico: Variable '{name}' no declarada.")

# Crear una tabla de símbolos
symbol_table = SymbolTable()

# Programa de ejemplo
program = [
    ("int", "x"),
    ("int", "y"),
    ("x", "=", 5),
    ("y", "=", "x + 2"),
    ("z", "=", "x + y"),  # Error: 'z' no está declarada antes de usarla
]

# Análisis semántico
for line in program:
    if isinstance(line, tuple):
        data_type, variable_name = line
        symbol_table.declare_variable(variable_name, data_type)
    elif isinstance(line, str):
        symbol_table.check_variable(line)
    else:
        variable_name, _, expression = line
        symbol_table.check_variable(variable_name)
        # Realizar análisis semántico adicional para la expresión (opcional)

print("Análisis semántico exitoso. El programa es semánticamente válido.")
