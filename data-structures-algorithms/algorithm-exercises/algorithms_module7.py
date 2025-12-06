import heapq
import random

def dijkstra(graph, start, end):
    queue = []
    heapq.heappush(queue, (0, start))
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous = {node: None for node in graph}
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_node == end:
            break
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current_node
                heapq.heappush(queue, (new_distance, neighbor))
    path = []
    node = end
    while node is not None:
        path.append(node)
        node = previous[node]
    path.reverse()
    return path, distances[end]

def simulate_traffic_adjustment(graph):
    adjusted_graph = {}
    for node in graph:
        adjusted_graph[node] = {}
        for neighbor, base_weight in graph[node].items():
            traffic_factor = random.uniform(1.0, 1.5)
            adjusted_graph[node][neighbor] = base_weight * traffic_factor
    return adjusted_graph

def main():
    base_graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'C': 1, 'D': 5},
        'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
        'D': {'B': 5, 'C': 8, 'E': 2, 'F': 6},
        'E': {'C': 10, 'D': 2, 'F': 3, 'G': 7},
        'F': {'D': 6, 'E': 3, 'G': 2, 'H': 9},
        'G': {'E': 7, 'F': 2, 'H': 1, 'I': 3},
        'H': {'F': 9, 'G': 1, 'I': 4, 'J': 6},
        'I': {'G': 3, 'H': 4, 'J': 2, 'K': 5},
        'J': {'H': 6, 'I': 2, 'K': 4, 'L': 7},
        'K': {'I': 5, 'J': 4, 'L': 3, 'M': 8},
        'L': {'J': 7, 'K': 3, 'M': 2, 'N': 4},
        'M': {'K': 8, 'L': 2, 'N': 1, 'O': 6},
        'N': {'L': 4, 'M': 1, 'O': 2, 'P': 5},
        'O': {'M': 6, 'N': 2, 'P': 3, 'Q': 7},
        'P': {'N': 5, 'O': 3, 'Q': 4, 'R': 6},
        'Q': {'O': 7, 'P': 4, 'R': 2, 'S': 5},
        'R': {'P': 6, 'Q': 2, 'S': 3, 'T': 8},
        'S': {'Q': 5, 'R': 3, 'T': 1, 'U': 4},
        'T': {'R': 8, 'S': 1, 'U': 3, 'V': 7},
        'U': {'S': 4, 'T': 3, 'V': 2, 'W': 6},
        'V': {'T': 7, 'U': 2, 'W': 3, 'X': 5},
        'W': {'U': 6, 'V': 3, 'X': 2, 'Y': 4},
        'X': {'V': 5, 'W': 2, 'Y': 1, 'Z': 3},
        'Y': {'W': 4, 'X': 1, 'Z': 2},
        'Z': {'X': 3, 'Y': 2}
    }
    print("Hello! Welcome to the Food Delivery Route App")
    print("Available locations: A through Z")
    start = input("Enter your starting location (example- A, B,): ").strip().upper()
    end = input("Enter your destination: ").strip().upper()
    if start not in base_graph or end not in base_graph:
        print("Invalid location entered. Please restart and choose from the available options.")
        return
    graph_with_traffic = simulate_traffic_adjustment(base_graph)
    route, travel_time = dijkstra(graph_with_traffic, start, end)
    print("\nOptimal Route:", route)
    print(f"Estimated Travel Time (adjusted for traffic): {travel_time:.2f} minutes")

if __name__ == "__main__":
    main()
