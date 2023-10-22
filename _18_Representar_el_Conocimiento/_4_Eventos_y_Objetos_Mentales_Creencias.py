# Crear una estructura para representar creencias
creencias = {
    "Juan": {
        "cree_que": {
            "el cielo_es_azul": True,
            "los gatos_pueden_volar": False,
            "la pizza_es_deliciosa": True
        }
    },
    "María": {
        "cree_que": {
            "el cielo_es_azul": True,
            "los gatos_pueden_volar": True,
            "la pizza_es_deliciosa": False
        }
    }
}

# Mostrar las creencias de Juan
print("Creencias de Juan:")
for creencia, valor in creencias["Juan"]["cree_que"].items():
    print(f"{creencia}: {valor}")

# Mostrar las creencias de María
print("\nCreencias de María:")
for creencia, valor in creencias["María"]["cree_que"].items():
    print(f"{creencia}: {valor}")
