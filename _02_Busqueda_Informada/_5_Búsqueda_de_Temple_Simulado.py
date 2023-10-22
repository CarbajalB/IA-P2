import math
import random

def energy(x):
    return x**2
temperatura_inicial = 1000
temperatura_minima = 0.1
factor_enfriamiento = 0.9
iteraciones_por_temperatura = 100

x = random.uniform(-10, 10)  
energia_actual = energy(x)
mejor_x = x
mejor_energia = energia_actual
temperatura = temperatura_inicial
while temperatura > temperatura_minima:
    for _ in range(iteraciones_por_temperatura):
        vecino_x = x + random.uniform(-1, 1)
        energia_vecino = energy(vecino_x)
        delta_energia = energia_vecino - energia_actual
        if delta_energia < 0 or random.random() < math.exp(-delta_energia / temperatura):
            x = vecino_x
            energia_actual = energia_vecino
        if energia_actual < mejor_energia:
            mejor_x = x
            mejor_energia = energia_actual
    temperatura *= factor_enfriamiento

print("Mejor solucion encontrada: x =", mejor_x)
print("Energia minima:", mejor_energia)