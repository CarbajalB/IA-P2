import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# Cargamos un conjunto de datos de ejemplo (Iris dataset)
iris = datasets.load_iris()
X = iris.data[:, :2]  # Tomamos solo las dos primeras características para la visualización
y = iris.target

# Dividimos los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Creamos un clasificador SVM con un kernel lineal
svm_classifier = SVC(kernel='linear', C=1)

# Ajustamos el modelo a los datos de entrenamiento
svm_classifier.fit(X_train, y_train)

# Realizamos predicciones en los datos de prueba
y_pred = svm_classifier.predict(X_test)

# Evaluamos el rendimiento del modelo
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, y_pred)
print("Exactitud del SVM (kernel lineal):", accuracy)

# Visualizamos la frontera de decisión
def plot_decision_boundary(X, y, classifier, title):
    h = .02  # Tamaño del paso en la malla
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    Z = classifier.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, cmap=plt.cm.Spectral, alpha=0.8)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Spectral)
    plt.title(title)
    plt.show()

plot_decision_boundary(X_train, y_train, svm_classifier, "Frontera de decisión (SVM, kernel lineal)")