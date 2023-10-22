# Probabilidad de tener la enfermedad
P_A = 0.01
# Probabilidad de obtener un resultado positivo en la prueba si tienes la enfermedad
P_B_dado_A = 0.95
# Probabilidad de obtener un resultado positivo en la prueba si no tienes la enfermedad
P_B_dado_no_A = 0.05
# Aplicar la Regla de Bayes para calcular la probabilidad
P_A_dado_B = (P_B_dado_A * P_A) / ((P_B_dado_A * P_A) + (P_B_dado_no_A * (1 - P_A)))
print("Probabilidad de tener la enfermedad dado un resultado positivo en la prueba:", P_A_dado_B)