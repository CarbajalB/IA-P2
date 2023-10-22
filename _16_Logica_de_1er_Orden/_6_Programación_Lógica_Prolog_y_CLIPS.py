from pyswip import Prolog
from pyclips import Environment, Symbol
#PROLOG
def prolog_():
    prolog = Prolog()
    # Definir relaciones en Prolog
    prolog.assertz("padre(juan, maria)")
    prolog.assertz("padre(juan, pedro)")
    prolog.assertz("madre(ana, pedro)")
    # Consultas en Prolog
    for solucion in prolog.query("padre(juan, X)"):
        print("Juan es padre de", solucion["X"])
    for solucion in prolog.query("madre(X, pedro)"):
        print(solucion["X"], "es madre de Pedro")

#CLIPS 
def clips(): 
    # Crear un entorno CLIPS
    env = Environment()
    # Definir reglas y hechos en CLIPS
    env.build("""
        (defrule regla-1
            (manzana-roja)
            =>
            (assert (fruta "manzana" "roja"))
        )

        (assert (manzana-roja))
    """)
    # Ejecutar el entorno
    env.run()
    # Consultar hechos
    for hecho in env.assertions():
        print(hecho)
    # Consultar hechos específicos
    consulta = env.find_fact('fruta', ("manzana", "roja"))
    if consulta:
        print("Fruta encontrada:", consulta)
    # Limpiar el entorno
    env.reset()

op=input("Que tipo de programacion logica deseas intentar: \n1.-Prolog\n2.-Clips\n")
if op == '1':
    prolog_()
elif op == '2':
    clips()
else:
    print("No existe esa opcion :)")
