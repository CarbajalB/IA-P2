from rdflib import Graph, URIRef, Literal
from rdflib.namespace import RDF, RDFS

# Crear un nuevo grafo RDF
g = Graph()

# Definir un recurso y su tipo
persona = URIRef("http://example.org/persona")
g.add((persona, RDF.type, RDFS.Class))

# Definir propiedades
nombre = URIRef("http://example.org/nombre")
apellido = URIRef("http://example.org/apellido")
edad = URIRef("http://example.org/edad")

# Agregar propiedades a la ontología
g.add((nombre, RDF.type, RDF.Property))
g.add((apellido, RDF.type, RDF.Property))
g.add((edad, RDF.type, RDF.Property))

# Definir relaciones entre recursos y propiedades
g.add((persona, nombre, Literal("Juan")))
g.add((persona, apellido, Literal("Pérez")))
g.add((persona, edad, Literal(30)))

# Consultar la ontología
for s, p, o in g:
    print(f"Triple: {s} {p} {o}")

# Guardar la ontología en un archivo RDF
g.serialize("ontologia.rdf")
