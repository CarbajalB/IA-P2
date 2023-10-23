# Espacio de Version
training_data = [
    {"edad": "joven", "genero": "masculino", "compra": "no"},
    {"edad": "joven", "genero": "femenino", "compra": "si"},
    {"edad": "media", "genero": "masculino", "compra": "no"},
    {"edad": "media", "genero": "femenino", "compra": "si"},
]

# Función para aprender una hipótesis utilizando AQ
def AQ_algorithm(examples):
    # Inicialmente, consideramos todas las restricciones posibles en el espacio de versiones
    version_space = [
        {"edad": "joven", "genero": "masculino"},
        {"edad": "joven", "genero": "femenino"},
        {"edad": "media", "genero": "masculino"},
        {"edad": "media", "genero": "femenino"},
    ]
    
    # Para cada ejemplo, eliminamos las restricciones inconsistentes con el ejemplo
    for example in examples:
        label = example["compra"]
        for version in version_space[:]:
            if (version["edad"] == example["edad"] and version["genero"] == example["genero"] and label == "no") or \
               (version["edad"] != example["edad"] or version["genero"] != example["genero"] and label == "si"):
                version_space.remove(version)

    # La hipótesis final es el espacio de versiones reducido
    return version_space

# Aprender una hipótesis a partir de ejemplos
hipotesis_aprendida = AQ_algorithm(training_data)
print("Hipótesis Aprendida:", hipotesis_aprendida)
