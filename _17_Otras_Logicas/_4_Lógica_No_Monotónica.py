class LogicaNoMonotona:
    def __init__(self):
        self.creencias = set()
        self.excepciones = set()

    def agregar_creencia(self, creencia):
        self.creencias.add(creencia)

    def agregar_excepcion(self, excepcion):
        self.excepciones.add(excepcion)

    def verificar(self, creencia):
        if creencia in self.excepciones:
            return False
        return creencia in self.creencias

# Crear una instancia de lógica no monótona
sistema = LogicaNoMonotona()

# Inicialmente, creemos que "los pájaros vuelan"
sistema.agregar_creencia("Los pájaros vuelan")

# Verificar la creencia
print("¿Los pájaros vuelan? (Creencia inicial):", sistema.verificar("Los pájaros vuelan"))

# Agregar una excepción: los pingüinos no vuelan
sistema.agregar_excepcion("Los pingüinos no vuelan")

# Verificar la creencia nuevamente
print("¿Los pájaros vuelan? (Después de agregar excepción):", sistema.verificar("Los pájaros vuelan"))
print("¿Los pingüinos vuelan? (Después de agregar excepción):", sistema.verificar("Los pingüinos vuelan"))
