import sqlite3

COLUMN_PRODUCT = 0
COLUMN_DESCRIPTION = 1
COLUMN_QUANTITY = 2


def display_products_with_stock_levels():
    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()
    sql = "SELECT name, description, quantity " \
          "FROM product " \
          "NATURAL JOIN stock"
    cursor.execute(sql)
    records = cursor.fetchall()

    print(f"There are {len(records)} products in the catalogue.")
    print(f"The stock level for each product is as follows:")

    for record in records:
        print(f"Product: {record[COLUMN_PRODUCT]}")
        print(f"Description: {record[COLUMN_DESCRIPTION]}")
        print(f"Stock level: {record[COLUMN_QUANTITY]}")
        print()

    db.close()


def display_product_supplier():
    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()
    sql = "SELECT product.name, supplier.name  " \
          "FROM product " \
          "INNER JOIN supplier ON product.supplier_id = supplier.id"
    cursor.execute(sql)
    records = cursor.fetchall()

    for record in records:
        print(f"Product: {record[0]}, Supplier: {record[1]}")

    db.close()


def display_product_supplier_locations():
    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()
    sql = "SELECT product.name, supplier.name, location.city, location.country  " \
          "FROM product " \
          "INNER JOIN supplier ON product.supplier_id = supplier.id  " \
          "INNER JOIN location ON supplier.location_id = location.id"
    cursor.execute(sql)
    records = cursor.fetchall()

    for record in records:
        print(f"Product: {record[0]}, Supplier: {record[1]}, Supplier Location: {record[2]}, {record[3]}")

    db.close()


def display_products_missing_suppliers():
    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()
    sql = "SELECT product.name, supplier.name  " \
          "FROM product " \
          "LEFT OUTER JOIN supplier ON product.supplier_id = supplier.id;"
    cursor.execute(sql)
    records = cursor.fetchall()

    for record in records:
        print(f"Product: {record[0]}, Supplier: {record[1]}")

    db.close()


def display_suppliers_missing_products():
    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()
    sql = "SELECT supplier.name, product.name  " \
          "FROM supplier " \
          "LEFT OUTER JOIN product ON product.supplier_id = supplier.id;"
    cursor.execute(sql)
    records = cursor.fetchall()

    for record in records:
        print(f"Supplier: {record[0]}, Product: {record[1]}")

    db.close()


def display_missing_data():
    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()
    sql = "SELECT product.name as 'product_name', supplier.name as 'supplier_name' " \
          "FROM product " \
          "LEFT OUTER JOIN supplier ON product.supplier_id = supplier.id " \
          "UNION " \
          "SELECT product.name as 'product_name', supplier.name as 'supplier_name' " \
          "FROM supplier " \
          "LEFT OUTER JOIN product ON product.supplier_id = supplier.id;"
    cursor.execute(sql)
    records = cursor.fetchall()

    products_missing_suppliers = []
    suppliers_missing_products = []

    for record in records:
        if record[0] is None:
            suppliers_missing_products.append(record[1])
        elif record[1] is None:
            products_missing_suppliers.append(record[0])

    print(f"The following products are missing suppliers:")
    print(products_missing_suppliers)
    print()
    print(f"The following suppliers are missing products:")
    print(suppliers_missing_products)

    db.close()
