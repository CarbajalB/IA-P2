empleados = {
    101: {"nombre": "Juan", "departamento": "Ventas"},
    102: {"nombre": "Ana", "departamento": "TI"},
    103: {"nombre": "Carlos", "departamento": "RRHH"},
    104: {"nombre": "Luisa", "departamento": "Ventas"}
}

# Función para recuperar datos de empleados por número de empleado
def recuperar_empleado(numero_empleado):
    empleado = empleados.get(numero_empleado)
    if empleado:
        return empleado
    else:
        return "Empleado no encontrado"

# Recuperar datos de empleados
numero_empleado = 102
empleado = recuperar_empleado(numero_empleado)
print(f"Datos del empleado con numero {numero_empleado}: {empleado}")

