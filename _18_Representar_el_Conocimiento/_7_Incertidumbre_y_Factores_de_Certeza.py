class ReglaConIncertidumbre:
    def __init__(self, antecedente, consecuente, factor_certeza):
        self.antecedente = antecedente
        self.consecuente = consecuente
        self.factor_certeza = factor_certeza

    def aplicar(self, hechos):
        # Verificar si el antecedente de la regla es verdadero en los hechos
        antecedente_verdadero = all(ant in hechos for ant in self.antecedente)
        
        if antecedente_verdadero:
            # Si el antecedente es verdadero, aplicar el consecuente con el factor de certeza
            for cons in self.consecuente:
                hechos[cons] = self.factor_certeza

# Crear una base de reglas con incertidumbre
reglas_con_incertidumbre = [
    ReglaConIncertidumbre(["Llueve"], ["Calle Mojada"], 0.8),
    ReglaConIncertidumbre(["Niebla"], ["Baja Visibilidad"], 0.6),
    ReglaConIncertidumbre(["Llueve", "Niebla"], ["Condiciones Peligrosas"], 0.7),
]

# Hechos iniciales
hechos = {
    "Llueve": 0.9,  # Factor de certeza alto
    "Niebla": 0.7,  # Factor de certeza moderado
}

# Aplicar las reglas con incertidumbre
for regla in reglas_con_incertidumbre:
    regla.aplicar(hechos)

# Mostrar los hechos resultantes con sus factores de certeza
for hecho, factor_certeza in hechos.items():
    print(f"Hecho: {hecho}, Factor de Certeza: {factor_certeza}")
