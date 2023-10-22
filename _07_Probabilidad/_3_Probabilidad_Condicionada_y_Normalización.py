# Probabilidad de tener la enfermedad
prob_enfermedad = 0.01
prob_pos_A = 0.95
prob_pos_B = 0.90
prob_pos_no_A = 0.05
prob_pos_no_B = 0.10
# Calculamos la probabilidad de obtener un resultado positivo en ambas pruebas
prob_pos_A_B = prob_pos_A * prob_pos_B
pron_pos_no_A_B = prob_pos_no_A * prob_pos_no_B
# Usamos la probabilidad total para calcular la probabilidad de obtener un resultado positivo en ambas pruebas
res_prob_pos_A_B = (prob_enfermedad * prob_pos_A_B) + ((1 - prob_enfermedad) * pron_pos_no_A_B)
# Calculamos la probabilidad condicionada de tener la enfermedad dado que ambas pruebas dieron positivo
prob_enfermedad_pos_A_B = (prob_enfermedad * prob_pos_A_B) / res_prob_pos_A_B
print("Probabilidad de tener la enfermedad dado que ambas pruebas dieron positivo:", prob_enfermedad_pos_A_B)