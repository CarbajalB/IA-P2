import itertools 
ciudades = ["Guadalajara", "Puebla", "Monterrey"] 
distacias = { 
    ("Guadalajara", "Puebla"): 400,
    ("Guadalajara", "Monterrey"): 2000,
    ("Puebla", "Monterrey"): 4000,
    ("Puebla", "Guadalajara"): 2000,
    ("Monterrey", "Guadalajara"): 4000,
    ("Monterrey", "Puebla"): 400
}
def longitud_ruta(ruta):
    total_distacias = 0
    for i in range(1, len(ruta)):
        total_distacias += distacias[(ruta[i - 1], ruta[i])]
    return total_distacias

registro_ruta = None
distancia_mejor = float('inf')
tabu_list = []
for _ in range(1000):
    for perm in itertools.permutations(ciudades, 3):
        if perm not in tabu_list:
            current_length = longitud_ruta(perm)
            if current_length < distancia_mejor :
                registro_ruta = perm
                distancia_mejor  = current_length

                tabu_list.append(perm)

print("Mejor ruta encontrada:", registro_ruta)
print("Distancia total de viaje:", distancia_mejor)