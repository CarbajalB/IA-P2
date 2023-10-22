class MotorInferenciaNoMonotonico:
    def __init__(self):
        self.hechos = set()
        self.conocimiento_no_monotonico = set()

    def agregar_hecho(self, hecho):
        self.hechos.add(hecho)

    def agregar_conocimiento_no_monotonico(self, regla):
        self.conocimiento_no_monotonico.add(regla)

    def inferir(self, hecho):
        if hecho in self.hechos:
            return True

        for regla in self.conocimiento_no_monotonico:
            if regla.puede_aplicar(self.hechos, hecho):
                return True

        return False

class ReglaNoMonotonica:
    def __init__(self, antecedente, consecuente):
        self.antecedente = antecedente
        self.consecuente = consecuente

    def puede_aplicar(self, hechos, hecho):
        # Verificar si el antecedente de la regla es verdadero en los hechos
        antecedente_verdadero = all(ant in hechos for ant in self.antecedente)
        # Verificar si el consecuente no es falso en los hechos
        consecuente_no_falso = all(cons not in hechos for cons in self.consecuente)
        # La regla se aplica si el antecedente es verdadero y el consecuente no es falso
        return antecedente_verdadero and consecuente_no_falso

# Crear un motor de inferencia no monotónico
motor = MotorInferenciaNoMonotonico()

# Agregar hechos iniciales
motor.agregar_hecho("PuedeVolar")
motor.agregar_hecho("TienePlumas")

# Definir conocimiento no monotónico
regla1 = ReglaNoMonotonica(["Puede Volar"], ["Es Ave"])
motor.agregar_conocimiento_no_monotonico(regla1)

# Inferir nuevos hechos
nuevo_hecho = "Es Ave"
resultado = motor.inferir(nuevo_hecho)

if resultado:
    print(f"Se ha inferido que '{nuevo_hecho}' es verdadero.")
else:
    print(f"No se puede inferir que '{nuevo_hecho}' sea verdadero en este momento.")
