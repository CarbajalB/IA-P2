class KDecisionTree:
    def __init__(self):
        self.tree = {}

    def add_node(self, parent, condition, decision):
        if parent not in self.tree:
            self.tree[parent] = {}
        self.tree[parent][condition] = decision

    def predict(self, instance):
        current_node = self.tree
        while True:
            feature, value = next(iter(current_node.keys()))
            if instance[feature] == value:
                if isinstance(current_node[feature], dict):
                    current_node = current_node[feature]
                else:
                    return current_node[feature]
            else:
                return "Desconocido"

# Ejemplo de uso
kdt = KDecisionTree()

kdt.add_node("root", "edad=joven", "Compra Aprobada")
kdt.add_node("root", "edad=media", "Compra Rechazada")
kdt.add_node("edad=joven", "genero=masculino", "Compra Aprobada")
kdt.add_node("edad=joven", "genero=femenino", "Compra Aprobada")
kdt.add_node("edad=media", "genero=masculino", "Compra Rechazada")
kdt.add_node("edad=media", "genero=femenino", "Compra Aprobada")

nuevo_cliente = {"edad": "media", "genero": "femenino"}
decision = kdt.predict(nuevo_cliente)
print(f"Decisión para el nuevo cliente: {decision}")
