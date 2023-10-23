import ply.lex as lex

# Definición de tokens
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
)

# Reglas de expresiones regulares para tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# Ignorar caracteres en blanco
t_ignore = ' \t'

# Regla para números
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Regla para manejar errores
def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

# Construir el analizador léxico
lexer = lex.lex()

# Ejemplo de uso
data = "3 + 4 * (10 - 2)"
lexer.input(data)

# Imprimir los tokens reconocidos
for token in lexer:
    print(f"Token: {token.type}, Valor: {token.value}")
