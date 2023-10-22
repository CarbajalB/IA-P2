lista = [15, 20, 12, 30, 9]

# Usando un cuantificador "todos" para verificar si todos los elementos son mayores que 10
todos_mayores_que_10 = all(x > 10 for x in lista)

if todos_mayores_que_10:
    print("Todos los elementos son mayores que 10.")
else:
    print("Al menos un elemento no es mayor que 10.")

# Usando un cuantificador "algunos" para verificar si al menos un elemento es par
alguno_es_par = any(x % 2 == 0 for x in lista)

if alguno_es_par:
    print("Al menos un elemento es par.")
else:
    print("Ningún elemento es par.")