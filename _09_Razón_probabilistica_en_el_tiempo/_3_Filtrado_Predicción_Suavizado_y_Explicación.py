import numpy as np

# Definir las matrices del filtro de Kalman
A = 1  # Matriz de transición de estado
H = 1  # Matriz de observación
Q = 0.01  # Covarianza del proceso (ruido del estado)
R = 1  # Covarianza de la medición (ruido de la observación)

estado_predicho = 0  # Supongamos un estado inicial
covarianza_predicha = 1  # Supongamos una covarianza inicial

estados_filtrados = []
estados_predichos = []

# Datos de la serie de tiempo (simulados)
datos_observados = np.linspace(0, 100, 100)

# Filtro de Kalman
for observacion in datos_observados:
    # Predicción del estado
    estado_predicho = A * estado_predicho
    covarianza_predicha = A * covarianza_predicha * A + Q
    
    # Actualización del estado basada en la observación
    ganancia = covarianza_predicha * H / (H * covarianza_predicha * H + R)
    estado_filtrado = estado_predicho + ganancia * (observacion - H * estado_predicho)
    covarianza_filtrada = (1 - ganancia * H) * covarianza_predicha
    
    # Almacenar resultados
    estados_filtrados.append(estado_filtrado)
    estados_predichos.append(estado_predicho)
    
    # Actualizar el estado predicho para el siguiente paso
    estado_predicho = estado_filtrado
    covarianza_predicha = covarianza_filtrada
print("Estados filtrados:")
print(estados_filtrados)