from rdflib import Graph, URIRef, BNode, Literal, Namespace
from rdflib.namespace import FOAF, RDF
def si_expertos():
    #Sistemas Expertos
    # Base de conocimiento de un sistema experto de diagnóstico médico
    conocimiento_medico = {
        "fiebre": True,
        "dolor_de_garganta": False,
        "tos": True,
        "diagnostico": ""
    }
    # Reglas de inferencia
    if conocimiento_medico["fiebre"] and conocimiento_medico["tos"]:
        conocimiento_medico["diagnostico"] = "Gripe"
    elif conocimiento_medico["dolor_de_garganta"]:
        conocimiento_medico["diagnostico"] = "Infección de garganta"
    else:
        conocimiento_medico["diagnostico"] = "Causa desconocida"
    print("Diagnóstico médico:", conocimiento_medico["diagnostico"])


def si_recomendacion():
    #Sistemas de Recomendación
    # Base de conocimiento de usuarios y películas
    usuarios = {
        "Usuario1": {"Star Wars", "Indiana Jones", "The Matrix"},
        "Usuario2": {"Star Wars", "Harry Potter", "The Matrix"},
        "Usuario3": {"Indiana Jones", "Harry Potter"}
    }
    # Recomendación para un usuario específico
    usuario_objetivo = "Usuario2"
    recomendaciones = set()
    for usuario, peliculas in usuarios.items():
        if usuario != usuario_objetivo:
            recomendaciones.update(peliculas - usuarios[usuario_objetivo])
    print("Recomendaciones para", usuario_objetivo, ":", recomendaciones)

def ontologias():
    #Ontologías y RDF (Resource Description Framework)
    

    # Crear un grafo RDF
    g = Graph()

    # Definir un espacio de nombres personalizado
    ns = Namespace("http://example.org/")

    # Definir recursos (individuos)
    juan = ns.PersonaJuan
    ana = ns.PersonaAna
    miguel = ns.PersonaMiguel
    empresa = ns.EmpresaXYZ

    # Agregar afirmaciones al grafo RDF
    g.add((juan, RDF.type, FOAF.Person))
    g.add((ana, RDF.type, FOAF.Person))
    g.add((miguel, RDF.type, FOAF.Person))
    g.add((empresa, RDF.type, FOAF.Organization))

    g.add((juan, FOAF.name, Literal("Juan Pérez")))
    g.add((ana, FOAF.name, Literal("Ana Sánchez")))
    g.add((miguel, FOAF.name, Literal("Miguel García")))
    g.add((empresa, FOAF.name, Literal("Empresa XYZ")))

    g.add((juan, ns.trabajaPara, empresa))
    g.add((ana, ns.trabajaPara, empresa))
    g.add((miguel, ns.trabajaPara, empresa))

    # Consulta RDF
    for s, p, o in g:
        print(s, p, o)


op=input("Que tipo de ingenieria del conocimiento deseas intentar: \n1.-Sistemas Expertos\n2.-Sistemas de Recomendación\n3.-Ontologías y RDF (Resource Description Framework)\n")
if op == '1':
    si_expertos()
elif op == '2':
    si_recomendacion()
elif op == '3':
    ontologias()
else:
    print("No existe esa opcion :)")

