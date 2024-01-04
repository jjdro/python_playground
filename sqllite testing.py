
import sqlite3

# Connect to the database or create a new one
conn = sqlite3.connect('products.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table to store the product information
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT,
        price REAL,
        quantity INTEGER
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS d2Products (
        id INTEGER PRIMARY KEY,
        name TEXT,
        price REAL,
        quantity INTEGER
    )
''')

# Insert the 5 products into the table
products = [
    (1, 'Product 1', 10.99, 100),
    (2, 'Product 2', 19.99, 50),
    (3, 'Product 3', 5.99, 200),
    (4, 'Product 4', 7.99, 150),
    (5, 'Product 5', 12.99, 80)
]

d2Products = [
    (6, 'Product 6', 10.99, 100),
    (7, 'Product 7', 19.99, 50),
    (8, 'Product 8', 5.99, 200),
    (9, 'Product 9', 7.99, 150),
    (10, 'Product 10', 12.99, 80)
]

# Insert the d2Products into the table
# Check if the d2Products table is empty
cursor.execute('SELECT COUNT(*) FROM d2Products')
result = cursor.fetchone()
if result[0] == 0:
    cursor.executemany('INSERT INTO d2Products VALUES (?, ?, ?, ?)', d2Products)

# Commit the changes
conn.commit()

# Retrieve all rows from the d2Products table
cursor.execute('SELECT * FROM d2Products')
rows = cursor.fetchall()

# Print the rows
for row in rows:
    print(row)
cursor.execute('SELECT * FROM products')
rows = cursor.fetchall()

# Print the rows
for row in rows:
    print(row)

# Close the connection
conn.close()


