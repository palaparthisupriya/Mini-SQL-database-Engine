def apply_where(data, condition):
    if not condition:
        return data
    col, op, val = condition
    try:
        val = int(val)
    except:
        pass

    filtered = []
    for row in data:
        if col not in row:
            print(f"Error: Column '{col}' does not exist.")
            continue

        row_val = row[col]
        try:
            row_val = int(row_val)
        except:
            pass

        if op == ">" and row_val > val:
            filtered.append(row)
        elif op == "<" and row_val < val:
            filtered.append(row)
        elif op == "=" and row_val == val:
            filtered.append(row)
        elif op == ">=" and row_val >= val:
            filtered.append(row)
        elif op == "<=" and row_val <= val:
            filtered.append(row)
    return filtered

def apply_select(data, columns):
    if columns == ["*"]:
        return data
    return [{col: row[col] for col in columns if col in row} for row in data]

def apply_order_by(data, column):
    if not column:
        return data
    if column not in data[0]:
        print(f"Error: Column '{column}' does not exist.")
        return data
    return sorted(data, key=lambda x: x[column])

def apply_count(data, column):
    if column not in data[0]:
        print(f"Error: Column '{column}' does not exist.")
        return 0
    return len(data)
