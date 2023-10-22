class Lámpara:
    def __init__(self):
        self.estado = False  # Inicialmente apagada

    def encender(self):
        self.estado = True

    def apagar(self):
        self.estado = False

# Crear una lámpara
lampara = Lámpara()

# Definir una secuencia de eventos temporales
eventos = [
    ("encender", 0),  # Encender la lámpara en el tiempo 0
    ("apagar", 2),    # Apagar la lámpara en el tiempo 2
    ("encender", 4),  # Encender la lámpara en el tiempo 4
]

# Simular eventos temporales
for evento, tiempo in eventos:
    if evento == "encender":
        lampara.encender()
        print(f"Tiempo {tiempo}: La lámpara se ha encendido.")
    elif evento == "apagar":
        lampara.apagar()
        print(f"Tiempo {tiempo}: La lámpara se ha apagado.")

# Verificar el estado de la lámpara en diferentes momentos
print("Estado de la lámpara:")
for tiempo in range(5):
    print(f"Tiempo {tiempo}: Encendida" if lampara.estado else f"Tiempo {tiempo}: Apagada")
