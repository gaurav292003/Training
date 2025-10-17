import sqlite3
import pandas as pd

#Connect to database
conn = sqlite3.connect('retail.db')
cursor = conn.cursor()

#Create products table
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    ProductID TEXT PRIMARY KEY,
    ProductName TEXT,
    Category TEXT,
    Price REAL
)
''')


#Create customers table
cursor.execute('''
CREATE TABLE IF NOT EXISTS customers (
CustomerID TEXT,
Name TEXT,
Email TEXT,
Country TEXT
)
''')

conn.commit()

#Read From CSV
products= pd.read_csv(r"C:\Users\user1\PycharmProjects\MilestoneProject\data\products.csv")
customers = pd.read_csv(r"C:\Users\user1\PycharmProjects\MilestoneProject\data\customers.csv")

#Load into database
products.to_sql('products', conn, if_exists='replace', index=False)
customers.to_sql('customers', conn, if_exists='replace', index=False)

print("Data inserted successfully")

#Add a new product
cursor.execute("INSERT INTO products VALUES (?,?,?,?)", ('P105', 'Smartwatch', 'Electronics', 150))
conn.commit()
print("Data inserted successfully")

#Update product price
cursor.execute("UPDATE products SET price =? WHERE ProductID=?", (900, 'P101'))
conn.commit()
print("Product price updated")

#Delete a customer
cursor.execute("DELETE FROM customers WHERE CustomerID=?", ('C002',))
conn.commit()
print("Customer deleted successfully")

#List all customers from India
cursor.execute("SELECT * FROM customers WHERE Country ='India'")
for row in cursor.fetchall():
    print(row)


print(pd.read_sql("SELECT * FROM products", conn))
print(pd.read_sql("SELECT * FROM customers", conn))