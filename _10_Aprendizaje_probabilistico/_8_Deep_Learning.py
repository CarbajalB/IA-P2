import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split
X = np.random.rand(100, 1)
y = 2 * X + 1 + 0.1 * np.random.randn(100, 1)
# Dividimos los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Definimos una red neuronal simple con una capa
model = tf.keras.Sequential([
    tf.keras.layers.Dense(1, input_shape=(1,))
])
# Compilamos el modelo
model.compile(optimizer='sgd', loss='mean_squared_error')
# Entrenamos el modelo
model.fit(X_train, y_train, epochs=100, verbose=0)
# Evaluamos el rendimiento del modelo en los datos de prueba
loss = model.evaluate(X_test, y_test, verbose=0)
print("Pérdida en datos de prueba:", loss)
# Hacemos predicciones
y_pred = model.predict(X_test)

print("Predicciones:")
for i in range(5):
    print(f"Entrada: {X_test[i][0]}, Predicción: {y_pred[i][0]}, Real: {y_test[i][0]}")