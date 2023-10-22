class AgenteLogico:
    def __init__(self):
        self.edad_minima = 18
        self.compra_minima = 50

    def es_elegible_para_descuento(self, edad, monto_compra):
        if edad >= self.edad_minima and monto_compra >= self.compra_minima:
            return True
        else:
            return False

# Crear una instancia del agente lógico
agente = AgenteLogico()

# Datos del cliente
edad_cliente = 25
monto_compra_cliente = 60

# Consultar al agente para determinar si el cliente es elegible para un descuento
elegible = agente.es_elegible_para_descuento(edad_cliente, monto_compra_cliente)

# Tomar una decisión basada en la respuesta del agente
if elegible:
    print("El cliente es elegible para un descuento.")
else:
    print("El cliente no es elegible para un descuento.")
