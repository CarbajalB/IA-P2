def unificacion(s1, s2):
    if s1 == s2:
        return {}
    if isinstance(s1, str) and s1.islower():
        return {s1: s2}
    if isinstance(s2, str) and s2.islower():
        return {s2: s1}
    if isinstance(s1, tuple) and isinstance(s2, tuple):
        if len(s1) != len(s2):
            return None
        unificacion_total = {}
        for u, v in zip(s1, s2):
            u_subst = sustituir(unificacion_total, u)
            v_subst = sustituir(unificacion_total, v)
            u_unificacion = unificacion(u_subst, v_subst)
            if u_unificacion is None:
                return None
            unificacion_total.update(u_unificacion)
        return unificacion_total
    return None
def sustituir(unificacion, s):
    if not unificacion:
        return s
    if isinstance(s, tuple):
        return tuple(sustituir(unificacion, t) for t in s)
    if s in unificacion:
        return sustituir(unificacion, unificacion[s])
    return 
# Ejemplo de unificación
expresion1 = ('f', 'x', 'a')
expresion2 = ('f', 'y', 'y')
resultado = unificacion(expresion1, expresion2)
if resultado is None:
    print("No se puede unificar las expresiones.")
else:
    print("Unificación exitosa. La asignación de variables es:")
    for variable, valor in resultado.items():
        print(f"{variable}: {valor}")
