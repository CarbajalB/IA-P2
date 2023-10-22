import clips

# Inicializa el entorno CLIPS
env = clips.Environment()

# Carga el módulo de lógica difusa
env.build('(clear)')
env.build('(load "fuzzy.clp")')

# Definir las funciones de membresía y las reglas difusas
env.build('(deffuzzy luminosidad (x) \
             (triangular 0 0 50) \
             (triangular 50 100 100) \
           )')

env.build('(deffuzzy intensidad (x) \
             (triangular 0 0 50) \
             (triangular 50 100 100) \
           )')

env.build('(defrule ajustar-lampara \
             (luminosidad ?l) \
             (intensidad ?i) \
             (luminosidad baja) \
             (intensidad media) \
             => \
             (assert (lampara intensidad-alta)) \
           )')

# Definir hechos de entrada
env.assert_string('(luminosidad 30)')
env.assert_string('(intensidad 70)')

# Ejecutar el sistema
env.run()

# Obtener el resultado
resultados = env.facts()
for hecho in resultados:
    print(hecho)

# Cerrar el entorno CLIPS
env.destroy()
