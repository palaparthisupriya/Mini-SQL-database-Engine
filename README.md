# Mini-SQL-database-Engine
# In-Memory SQL Engine

This project implements a simplified SQL query engine in Python that runs entirely in memory. 
It can load CSV files and execute basic SQL queries such as SELECT, WHERE, ORDER BY, and COUNT(). 
The goal is to understand how SQL queries are processed internally by a database.
## Setup

1. Clone the repository:
   git clone https://github.com/palaparthisupriya/Mini-SQL-database-Engine
2. Navigate to the project directory:
   cd in_memory_sql_engine
3. (Optional) Create a virtual environment:
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
4. Install dependencies (optional, only if using tabulate):
   pip install -r requirements.txt
5. Run the CLI:
   python src/cli.py
   
## This engine supports a simplified subset of SQL:

1. SELECT statements:
   - SELECT * FROM table;
   - SELECT column1, column2 FROM table;

2. WHERE clause:
   - Single condition with operators: =, >, <, >=, <=
   - Example: SELECT name, age FROM users WHERE age > 25;

3. ORDER BY clause:
   - Example: SELECT name, age FROM users ORDER BY name;

4. Aggregation:
   - COUNT(column)
   - Example: SELECT COUNT(age) FROM users WHERE city = 'New York';

Limitations:
- No support for JOINs or nested queries.
- Only single WHERE conditions supported (AND/OR not implemented yet).
## Examples
1. SELECT name, age FROM users WHERE age > 25 ORDER BY name;

2. SELECT * FROM users;

3. SELECT COUNT(age) FROM users WHERE city = 'Chicago';
