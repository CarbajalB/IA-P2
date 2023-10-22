# Definición de la función Skolem
def skolem_func():
    # Esta función podría generar un individuo específico de alguna manera
    return "individuo_especifico"

# Fórmula original con cuantificador existencial
formula_original = "∃x (Humano(x) ∧ Amigo(x, Juan))"

# Reemplazar el cuantificador existencial con la función Skolem
formula_skolem = formula_original.replace("∃x", f"{skolem_func()}")

# Imprimir la fórmula resultante
print("Fórmula con Skolem:")
print(formula_skolem)

# Ahora puedes usar la fórmula con Skolem en tus cálculos lógicos
