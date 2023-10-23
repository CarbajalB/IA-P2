# Definición de una gramática causal simple
class CausalGrammar:
    def __init__(self):
        self.causal_rules = {}

    def add_causal_rule(self, cause, effect):
        if cause in self.causal_rules:
            self.causal_rules[cause].append(effect)
        else:
            self.causal_rules[cause] = [effect]

    def get_effects(self, cause):
        return self.causal_rules.get(cause, [])

# Crear una instancia de la gramática causal
causal_grammar = CausalGrammar()

# Agregar reglas causales
causal_grammar.add_causal_rule("lluvia", "crecimiento de plantas")
causal_grammar.add_causal_rule("riego", "crecimiento de plantas")
causal_grammar.add_causal_rule("sol", "secado del suelo")

# Obtener los efectos de una causa
cause = "lluvia"
effects = causal_grammar.get_effects(cause)
print(f"Efectos de '{cause}': {', '.join(effects)}")

cause = "viento"
effects = causal_grammar.get_effects(cause)
print(f"Efectos de '{cause}': {', '.join(effects)}")
