class SistemaExperto:
    def __init__(self):
        self.base_conocimiento = []
    
    def agregar_regla(self, regla):
        self.base_conocimiento.append(regla)
    
    def hacer_inferencia(self, hechos):
        resultados = set()
        for regla in self.base_conocimiento:
            if regla.cumple_condiciones(hechos):
                resultados.add(regla.consecuencia)
        return resultados

class Regla:
    def __init__(self, condiciones, consecuencia):
        self.condiciones = condiciones
        self.consecuencia = consecuencia
    
    def cumple_condiciones(self, hechos):
        return all(condicion in hechos for condicion in self.condiciones)

# Crear un sistema experto
sistema_experto = SistemaExperto()

# Agregar reglas a la base de conocimiento
sistema_experto.agregar_regla(Regla(["llueve", "frio"], "Usar Abrigo"))
sistema_experto.agregar_regla(Regla(["soleado"], "Usar Gorra"))
sistema_experto.agregar_regla(Regla(["nublado", "calor"], "Usar Protector Solar"))
sistema_experto.agregar_regla(Regla(["llueve", "calor"], "Llevar Paraguas"))

# Hechos iniciales
hechos = ["llueve", "calor"]

# Realizar inferencia
resultados = sistema_experto.hacer_inferencia(hechos)

# Mostrar conclusiones
print("Conclusiones:")
for conclusion in resultados:
    print(conclusion)
