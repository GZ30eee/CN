import networkx as nx
import matplotlib.pyplot as plt

# Create a graph (network topology)
G = nx.Graph()

# Add nodes (routers)
nodes = ['A', 'B', 'C', 'D', 'E', 'F']
G.add_nodes_from(nodes)

# Add edges (links between routers with weights)
edges = [
    ('A', 'B', 1), ('A', 'C', 4), ('B', 'C', 2), ('B', 'D', 5),
    ('C', 'D', 1), ('C', 'E', 3), ('D', 'E', 2), ('D', 'F', 6), ('E', 'F', 1)
]
G.add_weighted_edges_from(edges)

# Function to perform Dijkstra's algorithm and find the shortest path
def dijkstra_algorithm(graph, start_node, end_node):
    # Using NetworkX's built-in dijkstra function to find the shortest path
    length, path = nx.single_source_dijkstra(graph, start_node)
    return length[end_node], path[end_node]

# Visualize the network and the shortest path
def visualize_network(graph, shortest_path=None):
    pos = nx.spring_layout(graph)  # Position the nodes using a layout algorithm
    plt.figure(figsize=(8, 6))

    # Draw the network nodes and edges
    nx.draw(graph, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=12, font_weight="bold")

    # If a shortest path is given, highlight it in red
    if shortest_path:
        path_edges = list(zip(shortest_path, shortest_path[1:]))
        nx.draw_networkx_edges(graph, pos, edgelist=path_edges, edge_color="red", width=3)

    # Display the graph
    plt.title("Network Topology with Shortest Path")
    plt.show()

def main():
    # User input for start and end node
    start_node = input("Enter the start node: ")
    end_node = input("Enter the end node: ")

    # Perform Dijkstra's algorithm to find the shortest path and its length
    distance, path = dijkstra_algorithm(G, start_node, end_node)

    # Display the results
    print(f"Shortest path from {start_node} to {end_node}: {path}")
    print(f"Total distance: {distance}")

    # Visualize the network and the shortest path
    visualize_network(G, shortest_path=path)

if __name__ == "__main__":
    main()
