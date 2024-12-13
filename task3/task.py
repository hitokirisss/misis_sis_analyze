import csv
import sys
import math

def load_matrix_from_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        return [list(map(float, row)) for row in reader]

def compute_entropy(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    total_entropy = 0.0

    for row in matrix:
        for value in row:
            if value != 0:
                probability = value / (rows - 1)
                total_entropy -= probability * math.log2(probability)

    return round(total_entropy, 1)

def process_file(file_path):
    matrix = load_matrix_from_csv(file_path)
    return compute_entropy(matrix)

def main():
    if len(sys.argv) != 2:
        print("Usage: python task.py <path_to_csv_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    entropy = process_file(file_path)
    print(entropy)

if __name__ == "__main__":
    main()

