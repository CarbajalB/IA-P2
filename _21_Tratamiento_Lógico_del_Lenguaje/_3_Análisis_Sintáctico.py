import ply.yacc as yacc

# Lista de tokens
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
)

# Reglas de precedencia
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

# Reglas de producción
def p_expression(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | LPAREN expression RPAREN
                  | NUMBER'''
    if len(p) == 2:  # Es un número
        p[0] = p[1]
    elif p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]

# Manejo de errores
def p_error(p):
    print(f"Error de sintaxis en '{p.value}'")

# Construir el analizador sintáctico
parser = yacc.yacc()

# Evaluar una expresión
data = "3 + 4 * (10 - 2)"
result = parser.parse(data)
print(f"Resultado de la expresión: {result}")
