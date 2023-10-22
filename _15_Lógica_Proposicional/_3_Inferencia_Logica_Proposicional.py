import sympy

# Definir variables proposicionales
p = sympy.symbols('p')
q = sympy.symbols('q')

# Crear expresiones lógicas
expresion1 = p & q  # p AND q
expresion2 = ~p | q  # NOT p OR q

# Realizar inferencia lógica
inferencia = sympy.simplify(expresion1 | expresion2)  # (p AND q) OR (NOT p OR q)

# Mostrar la expresión de inferencia
print("Expresión de Inferencia:", inferencia)

# Evaluar la expresión de inferencia
valor_verdad = inferencia.subs({p: True, q: False})
print("Valor de verdad de la inferencia:", valor_verdad)


