# Datos de entrenamiento
data = [
    {"edad": "joven", "genero": "masculino", "compra": "no"},
    {"edad": "joven", "genero": "femenino", "compra": "si"},
    {"edad": "joven", "genero": "femenino", "compra": "si"},
    {"edad": "media", "genero": "masculino", "compra": "no"},
    {"edad": "media", "genero": "femenino", "compra": "si"},
    {"edad": "viejo", "genero": "masculino", "compra": "si"},
    {"edad": "viejo", "genero": "femenino", "compra": "no"},
    {"edad": "viejo", "genero": "masculino", "compra": "no"},
]

# Función para calcular la entropía
import math

def entropy(data):
    labels = [entry["compra"] for entry in data]
    label_counts = {label: labels.count(label) for label in set(labels)}
    total_entries = len(labels)
    ent = sum((-count / total_entries) * math.log(count / total_entries, 2) for count in label_counts.values())
    return ent

# Función para dividir los datos en función de una característica
def split_data(data, feature):
    values = set(entry[feature] for entry in data)
    split_data = {value: [] for value in values}
    for entry in data:
        value = entry[feature]
        split_data[value].append(entry)
    return split_data

# Función para calcular la ganancia de información
def information_gain(data, feature):
    ent_total = entropy(data)
    split_data_dict = split_data(data, feature)
    ent_split = sum((len(split_data) / len(data)) * entropy(split_data) for split_data in split_data_dict.values())
    return ent_total - ent_split

# Función para encontrar la característica con la mayor ganancia de información
def find_best_feature(data, features):
    return max(features, key=lambda feature: information_gain(data, feature))

# Clase para representar el árbol de decisión
class DecisionTree:
    def __init__(self):
        self.tree = {}

    def build_tree(self, data, features):
        if not data:
            return None
        if all(entry["compra"] == "si" for entry in data):
            return "si"
        if all(entry["compra"] == "no" for entry in data):
            return "no"
        if not features:
            return "no"
        best_feature = find_best_feature(data, features)
        remaining_features = [feature for feature in features if feature != best_feature]
        tree = {best_feature: {}}
        for value, subset in split_data(data, best_feature).items():
            subtree = self.build_tree(subset, remaining_features)
            tree[best_feature][value] = subtree
        return tree

    def train(self, data, features):
        self.tree = self.build_tree(data, features)

    def predict(self, entry):
        tree = self.tree
        while isinstance(tree, dict):
            root = next(iter(tree.keys()))
            tree = tree[root][entry[root]]
        return tree

# Entrenar un árbol de decisión
features = ["edad", "genero"]
tree = DecisionTree()
tree.train(data, features)

# Hacer predicciones
nuevo_cliente = {"edad": "joven", "genero": "masculino"}
resultado = tree.predict(nuevo_cliente)
print(f"Nuevo cliente: {nuevo_cliente}, Compra: {resultado}")
