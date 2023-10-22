import random
def incert():
    temperatura_real = 25.0 # Temperatura actual en grados Celsius con cierta incertidumbre
    incertidumbre = 1.0  # Grado de incertidumbre
    temperatura_medida = temperatura_real + random.uniform(-incertidumbre, incertidumbre)# Generamos una medición con incertidumbre
    print("Temperatura medida con incertidumbre:", temperatura_medida)