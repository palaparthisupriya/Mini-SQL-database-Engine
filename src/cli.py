from utils import load_csv
from parser import parse_query
from engine import apply_where, apply_select, apply_order_by, apply_count

def main():
    # Ask user for CSV file
    file_path = input("Enter CSV file path (e.g., data/users.csv): ").strip()
    data = load_csv(file_path)
    if not data:
        return

    # Get query
    query = input("Enter SQL query: ").strip()
    parsed = parse_query(query)

    # Execute query
    filtered = apply_where(data, parsed["where"])

    if parsed["count"]:
        result = [{"COUNT": apply_count(filtered, parsed["count_col"])}]
    else:
        selected = apply_select(filtered, parsed["select"])
        result = apply_order_by(selected, parsed["order_by"])

    # Print result
    print("\nQuery Result:")
    for row in result:
        print(row)

if __name__ == "__main__":
    main()
