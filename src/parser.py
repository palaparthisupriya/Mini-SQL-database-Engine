def parse_query(query):
    """
    Parse a simple SQL query into components.
    Supports: SELECT, WHERE (single condition), ORDER BY, COUNT(column)
    """
    query = query.strip().lower()

    # SELECT part
    select_part = query.split("from")[0].replace("select","").strip()
    columns = [col.strip() for col in select_part.split(",")]

    # WHERE part
    where_part = None
    if "where" in query:
        where_clause = query.split("where")[1].split("order by")[0].strip()
        for op in [">=", "<=", ">", "<", "="]:
            if op in where_clause:
                col, val = where_clause.split(op)
                where_part = (col.strip(), op, val.strip())
                break

    # ORDER BY part
    order_by_part = None
    if "order by" in query:
        order_by_part = query.split("order by")[1].strip()

    # Check if COUNT is used
    is_count = False
    count_col = None
    for col in columns:
        if "count(" in col:
            is_count = True
            count_col = col.replace("count(", "").replace(")", "").strip()
            columns = ["COUNT"]  # Placeholder for engine

    return {
        "select": columns,
        "where": where_part,
        "order_by": order_by_part,
        "count": is_count,
        "count_col": count_col
    }
