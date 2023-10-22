class LogicaPorDefecto:
    def __init__(self):
        self.creencias = {"Los pájaros vuelan"}
        self.excepciones = set()

    def agregar_creencia(self, creencia):
        self.creencias.add(creencia)

    def agregar_excepcion(self, excepcion):
        self.excepciones.add(excepcion)

    def verificar(self, creencia):
        if creencia in self.excepciones:
            return False
        return creencia in self.creencias
# Crear una instancia de lógica por defecto
sistema = LogicaPorDefecto()
# Verificar la creencia por defecto
print("¿Los pájaros vuelan? (Por defecto):", sistema.verificar("Los pájaros vuelan"))
# Agregar una excepción: los pingüinos no vuelan
sistema.agregar_excepcion("Los pingüinos no vuelan")
# Verificar la creencia nuevamente
print("¿Los pájaros vuelan? (Después de agregar excepción):", sistema.verificar("Los pájaros vuelan"))
print("¿Los pingüinos vuelan? (Después de agregar excepción):", sistema.verificar("Los pingüinos vuelan"))
# Agregar una nueva creencia: evidencia de que los avestruces no vuelan
sistema.agregar_creencia("Los avestruces no vuelan")
# Verificar nuevamente la creencia por defecto
print("¿Los pájaros vuelan? (Después de agregar creencia):", sistema.verificar("Los pájaros vuelan"))
