class MundoPosible:
    def __init__(self, proposiciones):
        self.proposiciones = proposiciones
        self.necesario = set()
        self.posible = set()

    def es_necesario(self, proposicion):
        self.necesario.add(proposicion)

    def es_posible(self, proposicion):
        self.posible.add(proposicion)

    def evaluar(self, proposicion):
        if proposicion in self.necesario:
            return True
        if proposicion in self.posible:
            return True
        if proposicion in self.proposiciones:
            return True
        return False

# Definir proposiciones y mundos posibles
mundos = [
    MundoPosible({"A"}),
    MundoPosible({"B"}),
    MundoPosible({"C"}),
]

# En el primer mundo, es necesario que "A" sea verdadero
mundos[0].es_necesario("A")

# En el segundo mundo, es posible que "A" sea verdadero
mundos[1].es_posible("A")

# Evaluar si "A" es verdadero en cada mundo
for i, mundo in enumerate(mundos):
    resultado = mundo.evaluar("A")
    print(f"En el Mundo {i + 1}, A es verdadero: {resultado}")
