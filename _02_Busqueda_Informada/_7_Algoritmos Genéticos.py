import random

def fitness(x):
    return x**2
tama_poblacion = 100
probabilidad_mutacion = 0.1
num_generaciones = 100
poblacion = [random.uniform(-5, 5) for _ in range(tama_poblacion)]
for generacion in range(num_generaciones):
    nueva_poblacion = []
    for _ in range(tama_poblacion):
        padre1 = random.choice(poblacion)
        padre2 = random.choice(poblacion)
        hijo = (padre1 + padre2) / 2
        if random.random() < probabilidad_mutacion:
            hijo += random.uniform(-0.1, 0.1)
        nueva_poblacion.append(hijo)
    poblacion = nueva_poblacion
mejor_solucion = min(poblacion, key=fitness)
mejor_valor = fitness(mejor_solucion)

print("Mejor solucion encontrada: x =", mejor_solucion)
print("Valor maximo encontrado:", mejor_valor)


