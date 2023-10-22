import numpy as np
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Cargamos el conjunto de datos Iris
iris = load_iris()
X, y = iris.data, iris.target
# Dividimos los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Creamos un clasificador k-NN con k=3
knn = KNeighborsClassifier(n_neighbors=3)
# Ajustamos el modelo a los datos de entrenamiento
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
# Evaluamos el rendimiento del modelo k-NN
accuracy = accuracy_score(y_test, y_pred)
print("Exactitud (k-NN):", accuracy)
# Generamos datos de ejemplo
np.random.seed(0)
X = np.random.rand(100, 2)
# Creamos un modelo k-Means con 3 clústeres
kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(X)
# Obtenemos las etiquetas de los clústeres y los centroides
labels = kmeans.labels_
centroids = kmeans.cluster_centers_
# Visualizamos los datos y los clústeres
plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', s=200, linewidths=3, color='red')
plt.title("Clustering con k-Means")
plt.show()