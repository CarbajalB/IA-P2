class KDecisionList:
    def __init__(self):
        self.rules = []

    def add_rule(self, condition, decision):
        self.rules.append((condition, decision))

    def predict(self, instance):
        for condition, decision in self.rules:
            if all(instance[feature] == value for feature, value in condition.items()):
                return decision
        # Si ninguna regla coincide, devolver una decisión predeterminada
        return "Desconocido"

# Ejemplo de uso
kdl = KDecisionList()

kdl.add_rule({"edad": "joven", "genero": "masculino"}, "Compra Aprobada")
kdl.add_rule({"edad": "joven", "genero": "femenino"}, "Compra Aprobada")
kdl.add_rule({"edad": "media", "genero": "masculino"}, "Compra Rechazada")
kdl.add_rule({"edad": "media", "genero": "femenino"}, "Compra Aprobada")

nuevo_cliente = {"edad": "joven", "genero": "masculino"}
decision = kdl.predict(nuevo_cliente)
print(f"Decisión para el nuevo cliente: {decision}")
