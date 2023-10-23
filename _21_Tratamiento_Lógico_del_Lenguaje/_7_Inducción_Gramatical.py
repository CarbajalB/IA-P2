from pyleri import Grammar, Token

# Define la gramática
grammar = Grammar()
NUMBER = Token(re="\\d+")

@grammar.element()
def numbers():
    return NUMBER, ' '

# Analizar la entrada
input_string = "42 12 99"
result = numbers.parse_str(input_string)

if result.is_valid:
    numbers_list = [int(token.string) for token in result.children]
    print("Números encontrados:", numbers_list)
else:
    print("No se pudo analizar la entrada.")
