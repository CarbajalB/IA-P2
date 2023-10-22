import sympy
p = sympy.symbols('p')
q = sympy.symbols('q')

# Definir dos expresiones lógicas
expresion1 = p | q
expresion2 = q & p

# Verificar si son equivalentes
equivalencia = expresion1.equiv(expresion2)
print("¿Son equivalentes? ", equivalencia)

expresion = sympy.Implies(sympy.And(p, q), q)

# Verificar si es válida
es_valida = expresion.is_valid()
print("¿Es válida? ", es_valida)

expresion = sympy.And(p, q)

# Verificar si es satisfacible
es_satisfacible = expresion.satisfiable()
print("¿Es satisfacible? ", es_satisfacible)

