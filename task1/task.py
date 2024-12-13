import csv
import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: python script.py <csv_file_path> <row_number> <column_number>")
        return

    file_path = sys.argv[1]
    try:
        row_number = int(sys.argv[2])
        column_number = int(sys.argv[3])
    except ValueError:
        print("Error: Row and column numbers must be integers.")
        return

    try:
        with open(file_path, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)

            for current_row_index, row in enumerate(csv_reader, start=1):
                if current_row_index == row_number:
                    if column_number < 1 or column_number > len(row):
                        print(f"Error: Column {column_number} is out of range.")
                        return
                    print(row[column_number - 1])
                    return

            print(f"Error: Row {row_number} is out of range.")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

