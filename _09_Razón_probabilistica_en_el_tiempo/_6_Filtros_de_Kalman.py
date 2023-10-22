import numpy as np

def transicion_estado(estado_anterior):
    ruido_transicion = np.random.normal(0, 0.1) 
    nuevo_estado = estado_anterior + 1 + ruido_transicion
    return nuevo_estado

# Función de observación
def observacion(estado):
    # Simulación de medición
    ruido_observacion = np.random.normal(0, 1)  # Ruido de la observación
    return estado + ruido_observacion
num_particulas = 100
particulas = np.random.uniform(0, 1, num_particulas)
pesos = np.ones(num_particulas) / num_particulas
observaciones = [3, 4, 5]

# Ciclo principal del filtro de partículas
for observacion_actual in observaciones:
    # Actualizar las partículas
    for i in range(num_particulas):
        particulas[i] = transicion_estado(particulas[i])
        prob_observacion = observacion(particulas[i])
        pesos[i] *= np.exp(-0.5 * (observacion_actual - prob_observacion) ** 2)
    
    # Normalizar los pesos
    pesos /= np.sum(pesos)
    
    # Resampling (muestreo de partículas)
    indices_resample = np.random.choice(np.arange(num_particulas), size=num_particulas, p=pesos)
    particulas = particulas[indices_resample]
    pesos = np.ones(num_particulas) / num_particulas

estado_estimado = np.mean(particulas)

print("Estado estimado:", estado_estimado)