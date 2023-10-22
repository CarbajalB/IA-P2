prob_priori = 0.2  # Hay un 20% de probabilidad de tener una enfermedad
res_prueba = "positivo"
if res_prueba == "positivo":
    probapost = (prob_priori * 0.95) / ((prob_priori * 0.95) + ((1 - prob_priori) * 0.05))
else:
    probapost = (prob_priori * 0.05) / ((prob_priori * 0.05) + ((1 - prob_priori) * 0.95))
print("Probabilidad después de la prueba:", probapost)