lpcfg_grammar = {
    "S": [("NP VP", 1.0)],
    "NP": [
        ("Det N", 0.6),
        ("Pronoun", 0.4)
    ],
    "VP": [
        ("V NP", 0.7),
        ("VP PP", 0.3)
    ],
    "PP": [("P NP", 1.0)],
    "Det": {
        "the": 0.8,
        "a": 0.2
    },
    "N": {
        "cat": 0.4,
        "dog": 0.4,
        "bat": 0.2
    },
    "V": {
        "chased": 0.6,
        "saw": 0.4
    },
    "Pronoun": {
        "I": 0.4,
        "you": 0.3,
        "it": 0.2,
        "cats": 0.1
    },
    "P": {
        "with": 0.6,
        "in": 0.4
    }
}

sentence = "I saw the cat with a dog"

# Tokenización de la oración
tokens = sentence.split()

# Función para calcular la probabilidad de una oración
def calculate_sentence_probability(grammar, tokens):
    probability = 1.0
    for token in tokens:
        if token in grammar and isinstance(grammar[token], dict):
            continue  # Es una palabra con probabilidades en lugar de una categoría
        if token in grammar:
            probability *= grammar[token]
        else:
            return 0.0  # Si una palabra no está en la gramática, probabilidad cero
    return probability

probability = calculate_sentence_probability(lpcfg_grammar, tokens)
print("Probabilidad de la oracion:", probability)
