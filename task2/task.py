import csv
import sys
from collections import defaultdict, deque

def parse_edges_from_csv(file_path):
    edges = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        edges = [tuple(map(int, row)) for row in reader]
    return edges

def compute_relationships(edges, total_nodes):
    adjacency_list = defaultdict(list)
    reverse_adjacency_list = defaultdict(list)

    for parent, child in edges:
        adjacency_list[parent].append(child)
        reverse_adjacency_list[child].append(parent)

    relationships = [[0] * 5 for _ in range(total_nodes)]

    for parent, children in adjacency_list.items():
        for child in children:
            relationships[parent - 1][0] += 1  # Out-degree
            relationships[child - 1][1] += 1   # In-degree

    for node in range(1, total_nodes + 1):
        visited = set()
        queue = deque([(node, 0)])
        while queue:
            current, depth = queue.popleft()
            if current in visited:
                continue
            visited.add(current)
            if depth > 1:
                relationships[node - 1][2] += 1  # Indirect children
                relationships[current - 1][3] += 1  # Indirect parents
            for neighbor in adjacency_list[current]:
                if neighbor not in visited:
                    queue.append((neighbor, depth + 1))

    for node in range(1, total_nodes + 1):
        parents = reverse_adjacency_list[node]
        siblings = set()
        for parent in parents:
            siblings.update(adjacency_list[parent])
        siblings.discard(node)
        relationships[node - 1][4] = len(siblings)  # Sibling count

    return relationships

def generate_output(relationships):
    return '\n'.join([','.join(map(str, row)) for row in relationships])

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_csv_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    edges = parse_edges_from_csv(file_path)
    total_nodes = max(max(edge) for edge in edges)
    relationships = compute_relationships(edges, total_nodes)
    print(generate_output(relationships))

if __name__ == "__main__":
    main()
