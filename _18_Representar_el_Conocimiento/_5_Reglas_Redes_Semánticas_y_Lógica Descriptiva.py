from rdflib import Graph, URIRef
from rdflib.namespace import RDF, RDFS
from rdflib.plugins.sparql.parserutils import CompValue
from rdflib.plugins.sparql.sparql import CompValueOperator

def reglas():
    # Crear un grafo RDF
    g = Graph()
    # Definir reglas
    regla1 = """ 
            CONSTRUCT {
                ?x :esHijoDe ?y .
            }
            WHERE {
                ?x :tienePadre ?y .
            }
    """
    regla2 = """
            CONSTRUCT {
                ?x :esHijoUnicoDe ?y .
            }
            WHERE {
                ?x :tienePadre ?y .
                FILTER NOT EXISTS { ?z :tienePadre ?y . FILTER (?z != ?x) }
            }
    """
    # Cargar reglas en el grafo
    g.parse(data=regla1, format='sparql')
    g.parse(data=regla2, format='sparql')
    # Definir hechos
    g.add((URIRef('http://example.org/Alice'), URIRef('http://example.org/tienePadre'), URIRef('http://example.org/Bob')))
    g.add((URIRef('http://example.org/Bob'), URIRef('http://example.org/tienePadre'), URIRef('http://example.org/Charlie')))
    # Ejecutar las reglas
    resultado = g.query("""CONSTRUCT { ?x ?p ?o } WHERE { ?x ?p ?o }""")
    for tripleta in resultado:
        print(tripleta)

def log_des():
    # Crear un grafo RDF
    g = Graph()

    # Definir axiomas
    g.add((RDFS.subClassOf, RDF.type, RDFS.Class))
    g.add((RDFS.Resource, RDF.type, RDFS.Class))
    g.add((RDFS.subClassOf, RDFS.Class, RDFS.Resource))

    # Consultar axiomas
    consulta = g.query("""SELECT ?x WHERE { ?x rdf:type rdfs:Class }""")

    for resultado in consulta:
        print(resultado)

def red_semantica():
    # Crear un grafo RDF
    g = Graph()

    # Definir relaciones en la red semántica
    g.add((URIRef('http://example.org/Cat'), URIRef('http://example.org/isA'), URIRef('http://example.org/Animal')))
    g.add((URIRef('http://example.org/Dog'), URIRef('http://example.org/isA'), URIRef('http://example.org/Animal')))
    g.add((URIRef('http://example.org/Animal'), URIRef('http://example.org/eats'), URIRef('http://example.org/Food')))

    # Consultar la red semántica
    consulta = g.query("""SELECT ?x WHERE { ?x <http://example.org/isA> <http://example.org/Animal> }""")

    for resultado in consulta:
        print(resultado)

op=input("Que opcion deseas seleccionar: \n1.-Reglas\n2.-Redes Semanticas\n3.-Logica Descriptiva\n")
if op == '1':
    reglas()
elif op == '2':
    red_semantica()
elif op == '3':
    log_des()
else:
    print("No existe esa opcion :)")
