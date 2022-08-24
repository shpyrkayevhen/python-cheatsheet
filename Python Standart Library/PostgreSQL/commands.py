# Create db
'CREATE DATABASE shop;'

# Create table in shop db
'''CREATE TABLE product(
        id BIGSERIAL NOT NULL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        price INT NOT NULL,
        quantity INT NOT NULL,
);'''

# Insert data into db table
'''INSERT INTO product(name, price, quantity)
               VALUES ('IphoneX', 900, 34),
                      ('Samsung', 650, 25),
                      ('Xiaomi', 450, 51)
);'''


# Get all data from table
'''SELECT * FROM product;'''
# Get only product name from table
'''SELECT name FROM product;'''
# Get only price products whis name 'Iphone'
'''SELECT price FROM product WHERE name='Iphone'''


# Get products quantity from table
'''SELECT COUNT(id) FROM product;'''


# Update product price in products
'''UPDATE product SET price=1100 WHERE id=1;'''


# Delete product from products table
'''DELETE FROM product WHERE id=2;'''
# Multiply deliting in Python
# delete_script = '''DELETE FROM product WHERE id=%s'''
# delete_record = (1,)
# cursor.execute(delete_script, delete_record)


# BETWEEN
'''SELECT name, price FROM product WHERE id BETWEEN 5 AND 15;'''
'''SELECT name, price FROM product WHERE id NOT BETWEEN 5 AND 15;'''

# LIKE
