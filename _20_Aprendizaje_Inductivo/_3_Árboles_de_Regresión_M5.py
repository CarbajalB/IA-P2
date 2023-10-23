from Orange.regression import M5RegressionLearner
from Orange.data import Table

# Datos de entrenamiento de ejemplo
data = Table("housing.tab")  # Puedes reemplazar esto con tus propios datos

# Crear y entrenar el modelo M5
m5 = M5RegressionLearner()
m5_model = m5(data)

# Hacer predicciones con el modelo
new_data = Table("new_data.tab")  # Datos de entrada para hacer predicciones
predictions = m5_model(new_data)

# Imprimir las predicciones
for instance, prediction in zip(new_data, predictions):
    print(f"Características: {instance} - Predicción: {prediction}")
