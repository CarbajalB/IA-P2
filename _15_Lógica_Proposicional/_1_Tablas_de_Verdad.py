import sympy

# Definir variables proposicionales
p = sympy.symbols('p')
q = sympy.symbols('q')

# Crear expresiones lógicas
expresion1 = p & q  # p AND q
expresion2 = p | q  # p OR q
expresion3 = ~p  # NOT p

# Imprimir encabezado de la tabla de verdad
print("p\tq\t(p AND q)\t(p OR q)\t(NOT p)")

# Evaluar la tabla de verdad
for valor_p in [True, False]:
    for valor_q in [True, False]:
        resultado1 = expresion1.subs({p: valor_p, q: valor_q})
        resultado2 = expresion2.subs({p: valor_p, q: valor_q})
        resultado3 = expresion3.subs({p: valor_p})
        print(f"{valor_p}\t{valor_q}\t{resultado1}\t\t{resultado2}\t\t{resultado3}")

# Resultado esperado:
# p	q	(p AND q)	(p OR q)	(NOT p)
# True	True	True	True	False
# True	False	False	True	False
# False	True	False	True	True
# False	False	False	False	True
