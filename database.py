import sqlite3

def connect():
    return sqlite3.connect('products.db')

def create_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insert_product(name, description, quantity, price):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO products (name, description, quantity, price)
        VALUES (?, ?, ?, ?)
    ''', (name, description, quantity, price))
    conn.commit()
    conn.close()

def fetch_products():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_product(id, name, description, quantity, price):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE products
        SET name = ?, description = ?, quantity = ?, price = ?
        WHERE id = ?
    ''', (name, description, quantity, price, id))
    conn.commit()
    conn.close()

def delete_product(id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM products WHERE id = ?', (id,))
    conn.commit()
    conn.close()
