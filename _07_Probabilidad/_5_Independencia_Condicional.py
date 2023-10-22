# Generar todas las posibles combinaciones de lanzamientos de dos dados
posibles_lanzamientos = [(i, j) for i in range(1, 7) for j in range(1, 7)]
# Definir los eventos A, B y C
evento_A = [(i, j) for (i, j) in posibles_lanzamientos if (i + j) % 2 == 0]
evento_B = [(i, j) for (i, j) in posibles_lanzamientos if i % 2 == 1]
evento_C = [(i, j) for (i, j) in posibles_lanzamientos if j % 2 == 0]
# Verificar la independencia condicional de A y B dado C
independencia_condicional = all((i, j) in evento_A for i, j in evento_B if (i, j) in evento_C)
if independencia_condicional:
    print("Los eventos A y B son independientes dado C.")
else:
    print("Los eventos A y B no son independientes dado C.")