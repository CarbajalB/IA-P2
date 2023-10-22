import random
def f(x):
    return x**2
x = random.uniform(-10, 10)  
paso = 0.1  
num_iteraciones = 100  
for _ in range(num_iteraciones):
    actual = f(x)  
    izquierda = x - paso
    derecha = x + paso
    calidad_izquierda = f(izquierda)
    calidad_derecha = f(derecha)

    if calidad_izquierda < calidad_derecha and calidad_izquierda < actual:
        x = izquierda
    elif calidad_derecha < calidad_izquierda and calidad_derecha < actual:
        x = derecha
mejor_x = x
mejor_valor = f(x)

print("Mejor solucion encontrada: x =", mejor_x)
print("Valor minimo encontrado:", mejor_valor)