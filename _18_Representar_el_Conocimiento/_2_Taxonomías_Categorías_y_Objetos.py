# Definición de la clase base "Categoría"
class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.subcategorias = []

    def agregar_subcategoria(self, subcategoria):
        self.subcategorias.append(subcategoria)

    def __str__(self):
        return f"Categoría: {self.nombre}"

# Definición de la clase "Objeto" que hereda de "Categoría"
class Objeto(Categoria):
    def __init__(self, nombre, categoria_padre):
        super().__init__(nombre)
        self.categoria_padre = categoria_padre

    def __str__(self):
        return f"Objeto: {self.nombre}, Categoría: {self.categoria_padre.nombre}"

# Creación de categorías
animal = Categoria("Animal")
planta = Categoria("Planta")
objeto = Categoria("Objeto")

# Creación de objetos y asignación a categorías
perro = Objeto("Perro", animal)
gato = Objeto("Gato", animal)
rosa = Objeto("Rosa", planta)
silla = Objeto("Silla", objeto)

# Agregar subcategorías
animal.agregar_subcategoria(perro)
animal.agregar_subcategoria(gato)
planta.agregar_subcategoria(rosa)
objeto.agregar_subcategoria(silla)

# Mostrar la estructura de la taxonomía
def mostrar_taxonomia(categoria, nivel=0):
    print("  " * nivel + str(categoria))
    for subcategoria in categoria.subcategorias:
        mostrar_taxonomia(subcategoria, nivel + 1)

mostrar_taxonomia(animal)
