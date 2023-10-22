import numpy as np
data = np.array([
    [1, 2],
    [1.5, 1.8],
    [5, 8],
    [8, 8],
    [1, 0.6],
    [9, 11]
])

# Parámetros iniciales
k = 2  # Número de clusters
max_iter = 100  # Máximo de iteraciones
np.random.seed(0)
centroids = data[np.random.choice(data.shape[0], k, replace=False)]

# Función para asignar puntos a los clusters
def asignar_a_clusters(data, centroids):
    distances = np.linalg.norm(data[:, np.newaxis] - centroids, axis=2)
    return np.argmin(distances, axis=1)

# Algoritmo K-Means
for _ in range(max_iter):
    cluster_assignments = asignar_a_clusters(data, centroids)
    
    # Actualización de los centroides
    for i in range(k):
        if np.any(cluster_assignments == i):
            centroids[i] = np.mean(data[cluster_assignments == i], axis=0)
for i, centroid in enumerate(centroids):
    print(f"Cluster {i + 1} - Centroide: {centroid}")

for i in range(k):
    cluster_points = data[cluster_assignments == i]
    print(f"Puntos en el Cluster {i + 1}:\n{cluster_points}")