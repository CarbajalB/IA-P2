from functools import reduce

#Funciones Lambda
def lamda():
    numeros = [1, 2, 3, 4, 5]
    cuadrados = list(map(lambda x: x**2, numeros))
    print(cuadrados)  # Resultado: [1, 4, 9, 16, 25]

#Funcion Filter
def filter():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8]
    pares = list(filter(lambda x: x % 2 == 0, numeros))
    print(pares)  # Resultado: [2, 4, 6, 8]

#Funcion Reduce
def reduce():
    # Calcular la suma de una lista de números
    numeros = [1, 2, 3, 4, 5]
    suma = reduce(lambda x, y: x + y, numeros)
    print(suma)  # Resultado: 15

op=input("Que tipo de logicas de orden superior deseas intentar: \n1.-Funciones Lambda\n2.-Funcion Filter\n3.-Funcion Reduce\n")
if op == '1':
    lamda()
elif op == '2':
    filter()
elif op == '3':
    reduce()
else:
    print("No existe esa opcion :)")