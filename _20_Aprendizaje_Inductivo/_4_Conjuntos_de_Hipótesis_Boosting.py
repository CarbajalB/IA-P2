from sklearn.ensemble import AdaBoostClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Cargar el conjunto de datos Iris
iris = load_iris()
X, y = iris.data, iris.target

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear un clasificador base (en este caso, un árbol de decisión)
base_classifier = DecisionTreeClassifier(max_depth=1)

# Crear el clasificador AdaBoost
adaboost_classifier = AdaBoostClassifier(base_classifier, n_estimators=50, random_state=42)

# Entrenar el clasificador AdaBoost
adaboost_classifier.fit(X_train, y_train)

# Realizar predicciones
y_pred = adaboost_classifier.predict(X_test)

# Calcular la precisión del modelo
accuracy = accuracy_score(y_test, y_pred)
print(f"Precisión del modelo AdaBoost: {accuracy:.2f}")
