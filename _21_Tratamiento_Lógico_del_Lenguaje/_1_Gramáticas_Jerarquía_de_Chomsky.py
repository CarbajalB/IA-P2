n = 2
# Gramática de tipo 1 que genera el lenguaje anbncn (n ≥ 1)
# Reglas de producción: S -> aSBC | abC | ab

def generar_lenguaje_anbncn(n):
    if n < 1:
        return ""
    else:
        return "a" + generar_lenguaje_anbncn(n - 1) + "b" + generar_lenguaje_anbncn(n - 1) + "c"



# Gramática de tipo 2 para generar el lenguaje de paréntesis balanceados
# Reglas de producción: S -> (S) | SS | ε

def generar_parentesis_balanceados(n):
    if n == 0:
        return ""
    elif n == 1:
        return "()"
    else:
        return "(" + generar_parentesis_balanceados(n - 1) + ")" + generar_parentesis_balanceados(n - 1)



# Gramática de tipo 3 para generar el lenguaje de cadenas de 'a' y 'b' con un número par de 'a's
# Reglas de producción: S -> aS | bS | ε

def generar_cadenas_pares_de_as(n):
    if n == 0:
        return ""
    else:
        return "a" + generar_cadenas_pares_de_as(n - 1) + "b" + generar_cadenas_pares_de_as(n - 1)


op=input("Que gramatica deseas intentar:\n1.-Tipo 1\n2.-Tipo 2\n3.-Tipo 3\n")

if op == '1':
    cadena = generar_lenguaje_anbncn(n)
    print(cadena)
elif op == '2':
    cadena = generar_parentesis_balanceados(n)
    print(cadena)
elif op == '3':
    cadena = generar_cadenas_pares_de_as(n)
    print(cadena)
else:
    print("Esa opcion no existe :)")

