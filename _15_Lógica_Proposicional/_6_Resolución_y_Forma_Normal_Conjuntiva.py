import sympy

# Definición de variables proposicionales
p, q, r = sympy.symbols('p q r')

# Definición de la fórmula lógica
formula = (p | ~q) & (~p | q | r) & (p | ~r)

# Convertir la fórmula en su Forma Normal Conjuntiva (FNC)
fnc = sympy.to_cnf(formula)

# Mostrar la Fórmula Original
print("Fórmula Original:", formula)

# Mostrar la Fórmula en Forma Normal Conjuntiva (FNC)
print("Forma Normal Conjuntiva (FNC):", fnc)

# Resolución
resolver = sympy.satisfiable(fnc)
print("¿La FNC es satisfacible (resoluble)?:", resolver)
