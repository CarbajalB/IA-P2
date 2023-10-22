import numpy as np

# Definir las probabilidades de dos opciones
probabilidad_opcion_A = 0.7
probabilidad_opcion_B = 0.3

# Generar una decisión basada en las probabilidades
decision = np.random.choice(['Opcion A', 'Opcion B'], p=[probabilidad_opcion_A, probabilidad_opcion_B])

# Mostrar la decisión tomada
print(f"Decisión tomada: {decision}")
