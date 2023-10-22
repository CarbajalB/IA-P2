corpus = [
    "El perro es un animal domestico.",
    "Los gatos son animales independientes.",
    "Los pajaros vuelan en el cielo.",
    "Los libros son una fuente de conocimiento.",
    "La programacion es una habilidad valiosa.",
    "Los datos son importantes en la ciencia de datos.",
]

# Guardar el corpus en un archivo de texto
with open("corpus.txt", "w", encoding="utf-8") as file:
    for text in corpus:
        file.write(text + "\n")

# Leer el corpus desde el archivo de texto
with open("corpus.txt", "r", encoding="utf-8") as file:
    read_corpus = file.read()

print("Contenido del corpus:")
print(read_corpus)
