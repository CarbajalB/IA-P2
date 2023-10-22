import random
# Definir la distribución de probabilidad de una moneda justa
distribucion_moneda = {
    'C': 0.5,  # Probabilidad de cara
    'X': 0.5   # Probabilidad de cruz
}
# Generar una muestra aleatoria de la distribución
resultado = random.choices(list(distribucion_moneda.keys()), weights=distribucion_moneda.values())[0]
print("Resultado de la moneda:", resultado)