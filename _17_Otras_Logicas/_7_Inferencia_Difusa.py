import numpy as np
import matplotlib.pyplot as plt

# Funciones de pertenencia para las variables de entrada y salida
def pertenencia_luminosidad(x):
    if 0 <= x <= 50:
        return x / 50
    elif 50 < x <= 100:
        return 1 - ((x - 50) / 50)
    else:
        return 0

def pertenencia_intensidad(x):
    if 0 <= x <= 50:
        return x / 50
    elif 50 < x <= 100:
        return 1 - ((x - 50) / 50)
    else:
        return 0

# Reglas difusas
def regla1(luminosidad):
    return min(pertenencia_luminosidad(luminosidad), 0.7)

def regla2(luminosidad):
    return min(pertenencia_luminosidad(luminosidad), 0.3)

# Operador OR para combinar las reglas
def operador_or(regla1, regla2):
    return max(regla1, regla2)

# Universo de discurso
luminosidad = np.arange(0, 101, 1)

# Evaluar las reglas en el universo de discurso
resultado = np.array([operador_or(regla1(x), regla2(x)) for x in luminosidad])

# Visualizar el resultado
plt.plot(luminosidad, resultado, 'b', linewidth=1.5, label='Resultado')
plt.legend()
plt.xlabel('Luminosidad')
plt.ylabel('Grado de membresía')
plt.show()
