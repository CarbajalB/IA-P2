import networkx as nx
import matplotlib.pyplot as plt

def prim_mst(graph):
    mst = nx.Graph()
    start_node = list(graph.nodes())[0]

    visited = set([start_node])

    while len(visited) < len(graph.nodes()):
        edge_candidates = []
        for node in visited:
            edge_candidates.extend(graph.edges(node, data=True))

        edge_candidates = [edge for edge in edge_candidates if edge[1] not in visited]

        if not edge_candidates:
            break

        min_edge = min(edge_candidates, key=lambda x: x[2]['weight'])
        visited.add(min_edge[1])
        mst.add_edge(min_edge[0], min_edge[1], weight=min_edge[2]['weight'])

    return mst

# Crear un grafo de ejemplo con pesos en las aristas
G = nx.Graph()
edges = [('A', 'B', 2), ('A', 'D', 3), ('B', 'C', 1), ('B', 'A', 4), ('C', 'D', 5)]
G.add_weighted_edges_from(edges)

# Calcular el árbol parcial mínimo utilizando el algoritmo de Prim
mst = prim_mst(G)

# Dibujar el grafo original y el árbol parcial mínimo
pos = nx.spring_layout(G)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
nx.draw(mst, pos, node_size=500, node_color='lightcoral', width=2)
plt.show()
