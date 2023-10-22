import numpy as np
from scipy.signal import find_peaks
import matplotlib.pyplot as plt

# Definir un conjunto difuso triangular
x = np.linspace(0, 10, 100)
conjunto_difuso = np.zeros_like(x)
conjunto_difuso[x <= 2] = 0
conjunto_difuso[(x > 2) & (x <= 5)] = (x[(x > 2) & (x <= 5)] - 2) / 3
conjunto_difuso[x > 5] = 1

# Visualizar el conjunto difuso
plt.plot(x, conjunto_difuso)
plt.title("Conjunto Difuso Triangular")
plt.xlabel("X")
plt.ylabel("Grado de membresía")
plt.show()

# Encontrar los puntos máximos (cúspides) del conjunto difuso
peaks, _ = find_peaks(conjunto_difuso)
print("Puntos máximos (cúspides):", x[peaks])

# Calcular el grado de membresía de un valor en el conjunto difuso
valor = 4.0
grado_de_membresia = np.interp(valor, x, conjunto_difuso)
print(f"Grado de membresía de {valor} en el conjunto difuso: {grado_de_membresia}")
