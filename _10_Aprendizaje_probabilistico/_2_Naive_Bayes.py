datos = [
    ("gratis", "spam"),
    ("compra ahora", "spam"),
    ("gratis", "spam"),
    ("gratis", "no spam"),
    ("compra ahora", "no spam"),
    ("gratis", "no spam"),
]
# Función para calcular la probabilidad de clase
def probabilidad_clase(etiqueta, datos):
    total = len(datos)
    etiqueta_count = sum(1 for _, etiqueta in datos if etiqueta == etiqueta)
    return etiqueta_count / total
# Función para calcular la probabilidad condicional de una característica dada la clase
def probabilidad_condicional(caracteristica, etiqueta, datos):
    total = len(datos)
    caracteristica_count = sum(1 for feat, lbl in datos if feat == caracteristica and lbl == etiqueta)
    etiqueta_count = sum(1 for _, lbl in datos if lbl == etiqueta)
    return caracteristica_count / etiqueta_count
# Función para realizar la clasificación Naïve Bayes
def clasificador_naive_bayes(caracteristicas, datos):
    etiquetas = set(lbl for _, lbl in datos)
    mejor_etiqueta = None
    mejor_probabilidad = -1

    for etiqueta in etiquetas:
        prob_clase = probabilidad_clase(etiqueta, datos)
        prob_conjunta = prob_clase

        for caracteristica in caracteristicas:
            prob_conjunta *= probabilidad_condicional(caracteristica, etiqueta, datos)
        
        if prob_conjunta > mejor_probabilidad:
            mejor_etiqueta = etiqueta
            mejor_probabilidad = prob_conjunta

    return mejor_etiqueta
nuevas_caracteristicas = ["gratis", "compra ahora"]
resultado = clasificador_naive_bayes(nuevas_caracteristicas, datos)
print("Clase predicha:", resultado)