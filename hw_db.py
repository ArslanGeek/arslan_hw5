import sqlite3

def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return connection
def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)

def add_product(conn, product):
    sql = '''INSERT INTO products (product_title, price, quantity)
    VALUES (?, ?, ?)'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def select_all_products(conn):
    sql = '''SELECT * FROM products'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql)

        rows_list = cursor.fetchall()
        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)

def select_products_by_limit(conn, limit1, limit2):
    sql = '''SELECT * FROM products
    WHERE price <= ? and quantity >= ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (limit1, limit2,))

        rows_list = cursor.fetchall()
        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)

# def find_products_by_name(conn, name):
#     sql = '''SELECT * FROM products
#     WHERE product_title LIKE ? '''
#     try:
#         cursor = conn.cursor()
#         cursor.execute(sql, (name,))
#
#         rows_list = cursor.fetchall()
#         for row in rows_list:
#             print(row)
#
#     except sqlite3.Error as e:
#         print(e)

def find_products_by_name(conn, keyword):
    sql = '''SELECT * FROM products
    WHERE product_title LIKE ? OR product_title LIKE ?'''

    try:
        cursor = conn.cursor()

        keywordlow = '%'+keyword+'%'
        keywordupp = '%'+keyword.capitalize()+'%'

        cursor.execute(sql, (keywordupp, keywordlow))


        rows = cursor.fetchall()
        for row in rows:
            for i in row:
                print(i, end= ', ')
            print('\n')

    except sqlite3.Error as a:
        print(a)




def update_product(conn, product):
    sql = '''UPDATE products SET quantity = ?, price = ?
    WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def delete_product(conn, id):
    sql = '''DELETE FROM products WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)


sql_create_products_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL,
price FLOAT(10) NOT NULL DEFAULT 0.00,
quantity INTEGER NOT NULL DEFAULT 0
)
'''

connection_to_db = create_connection('hw.db')

if connection_to_db is not None:
    print(f'Successfully connected to Data Base!')
    # create_table(connection_to_db, sql_create_products_table)
    # add_product(connection_to_db, ('Ice cream', 2.99, 50))
    # add_product(connection_to_db, ('Socks', 10, 100))
    # add_product(connection_to_db, ('T-shirt', 80, 20))
    # add_product(connection_to_db, ('Powerbank', 30, 10))
    # add_product(connection_to_db, ('Coca-cola', 8.88, 45))
    # add_product(connection_to_db, ('Dress', 40, 23))
    # add_product(connection_to_db, ('Sofa', 400, 3))
    # add_product(connection_to_db, ('Pillows', 20, 10))
    # add_product(connection_to_db, ('Mirror', 100, 30))
    # add_product(connection_to_db, ('Bag', 28.99, 88))
    # add_product(connection_to_db, ('Smartphone', 677, 10))
    # add_product(connection_to_db, ('Charger', 40, 180))
    # add_product(connection_to_db, ('Shoes', 100, 30))
    # add_product(connection_to_db, ('Freeze', 800, 5))
    # add_product(connection_to_db, ('Olive oil', 18, 190))
    # select_all_products(connection_to_db)
    # change_products_quantity(connection_to_db, 100)
    # update_product(connection_to_db, (77, 59, 13))
    # select_products_by_limit(connection_to_db, 100, 5)
    # delete_product(connection_to_db, 2)
    # find_products_by_name(connection_to_db, 'cream')
    connection_to_db.close()




