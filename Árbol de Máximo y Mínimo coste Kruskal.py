import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo de ejemplo con pesos en las aristas
G = nx.Graph()
edges = [(1, 2, 1), (1, 3, 4), (2, 3, 2), (2, 4, 3), (3, 4, 1)]
G.add_weighted_edges_from(edges)

# Calcular el Árbol de Mínimo Coste (MST) usando Kruskal
mst = nx.minimum_spanning_tree(G)

# Calcular el Árbol de Máximo Coste (Maximum Spanning Tree) restando los pesos máximos a los pesos actuales
max_spanning_tree = G.copy()
for u, v, w in max_spanning_tree.edges(data=True):
    max_spanning_tree[u][v]['weight'] = -w['weight']

max_spanning_tree = nx.minimum_spanning_tree(max_spanning_tree)

# Dibujar el grafo original, el MST y el Maximum Spanning Tree
pos = nx.spring_layout(G)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

nx.draw(mst, pos, node_size=500, node_color='lightcoral', width=2)
plt.title("Árbol de Mínimo Coste (MST)")

plt.figure()
nx.draw(max_spanning_tree, pos, node_size=500, node_color='lightcoral', width=2)
plt.title("Árbol de Máximo Coste")

plt.show()
