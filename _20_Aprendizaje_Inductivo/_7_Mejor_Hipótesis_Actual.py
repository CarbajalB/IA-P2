class BestCurrentHypothesis:
    def __init__(self):
        self.hypothesis = None
        self.best_accuracy = 0.0

    def update_hypothesis(self, new_hypothesis, new_accuracy):
        if new_accuracy > self.best_accuracy:
            self.hypothesis = new_hypothesis
            self.best_accuracy = new_accuracy

# Ejemplo de uso
bch = BestCurrentHypothesis()

# Simulación de un proceso de aprendizaje inductivo
nuevas_hipotesis = [
    {"edad": "joven", "genero": "masculino", "accuracy": 0.8},
    {"edad": "joven", "genero": "femenino", "accuracy": 0.85},
    {"edad": "media", "genero": "masculino", "accuracy": 0.75},
    {"edad": "media", "genero": "femenino", "accuracy": 0.9},
]

for hipotesis in nuevas_hipotesis:
    bch.update_hypothesis(hipotesis, hipotesis["accuracy"])

mejor_hipotesis = bch.hypothesis
print("Mejor hipótesis:", mejor_hipotesis)
