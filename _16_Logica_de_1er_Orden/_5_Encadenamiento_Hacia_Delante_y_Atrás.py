# Base de conocimiento y reglas
base_conocimiento = {"llueve", "viento"}
reglas = [({"llueve"}, "paraguas"), ({"viento"}, "abrigo")]
meta = "abrigo"

#Encadenamiento Hacia Adelante
def encadenamiento_hacia_adelante(base_conocimiento, reglas):
    hechos_conocidos = base_conocimiento.copy()
    nuevos_hechos = set()

    while True:
        hecho_nuevo = False
        for regla in reglas:
            antecedentes, consecuente = regla
            if all(hecho in hechos_conocidos for hecho in antecedentes) and consecuente not in hechos_conocidos:
                hechos_conocidos.add(consecuente)
                nuevos_hechos.add(consecuente)
                hecho_nuevo = True
                print(f"Se aplicó la regla: {antecedentes} => {consecuente}")

        if not hecho_nuevo:
            break

    return hechos_conocidos, nuevos_hechos


#Encadenamiento Hacia Atras
def encadenamiento_hacia_atras(base_conocimiento, reglas, meta):
    hechos_conocidos = base_conocimiento.copy()

    def buscar_hechos_apoyo(hecho):
        if hecho in hechos_conocidos:
            return True
        for regla in reglas:
            antecedentes, consecuente = regla
            if consecuente == hecho and all(buscar_hechos_apoyo(a) for a in antecedentes):
                hechos_conocidos.add(hecho)
                print(f"Para llegar a la meta '{hecho}', se aplicó la regla: {antecedentes} => {consecuente}")
                return True
        return False

    if buscar_hechos_apoyo(meta):
        print(f"Se alcanzó la meta '{meta}'.")
    else:
        print(f"No se pudo alcanzar la meta '{meta}'.")



op=input("Que tipo de encadenamiento deseas intentar: \n1.-Hacia Delante\n2.-Hacia Atras\n")
if op == '1':
    nuevos_hechos_obtenidos, nuevos_hechos = encadenamiento_hacia_adelante(base_conocimiento, reglas)
    print("Hechos conocidos:", nuevos_hechos_obtenidos)
    print("Nuevos hechos deducidos:", nuevos_hechos)
elif op == '2':
    encadenamiento_hacia_atras(base_conocimiento, reglas, meta)
else:
    print("No existe esa opcion :)")