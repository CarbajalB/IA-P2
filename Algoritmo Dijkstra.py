import networkx as nx
import matplotlib.pyplot as plt
import heapq

def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight['weight']
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    path = []
    current_node = end
    while current_node != start:
        path.insert(0, current_node)
        for neighbor, weight in graph[current_node].items():
            if distances[current_node] == distances[neighbor] + weight['weight']:
                current_node = neighbor
                break
    path.insert(0, start)
    return path

# Crear un grafo de ejemplo
G = nx.Graph()
edges = [('A', 'B', 1), ('A', 'C', 4), ('B', 'D', 2), ('B', 'D', 5), ('C', 'D', 1)]
for edge in edges:
    G.add_edge(edge[0], edge[1], weight=edge[2])

# Encontrar la ruta más corta con Dijkstra
start_node = 'A'
end_node = 'D'
shortest_path = dijkstra(G, start_node, end_node)

# Dibujar el grafo
pos = nx.spring_layout(G)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw(G, pos, with_labels=True, node_size=800, node_color='lightblue')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
nx.draw_networkx_edges(G, pos, edgelist=[(shortest_path[i], shortest_path[i+1]) for i in range(len(shortest_path)-1)], edge_color='red', width=6)
plt.show()

print("Ruta más corta:", shortest_path)
