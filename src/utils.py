import csv

def load_csv(file_path):
    """
    Load a CSV file and return a list of dictionaries (rows).
    """
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            data = [row for row in reader]
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
