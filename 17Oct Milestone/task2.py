from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
import sqlite3

app= FastAPI(title="Retail Order Processing System")

#Database Connection
def get_connection():
    return sqlite3.connect("retail.db")

#Data Models
class Product(BaseModel):
    ProductID: str
    ProductName: str
    Category: str
    Price: float

class Customer(BaseModel):
    CustomerID: str
    Name: str
    Email: str
    Country: str



#Product Endpoints
@app.get("/products")
def get_products():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    rows= cursor.fetchall()
    conn.close()
    return rows

@app.post("/products")
def add_product(product: Product):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO products VALUES (?,?,?,?)",
                       (product.ProductID, product.ProductName, product.Category, product.Price))
        conn.commit()
        return{"message": "Product added successfully"}
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="Product ID already exists")
    finally:
        conn.close()

@app.put("/products/{ProductID}")
def update_product(product: Product):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET ProductName =?, Category =?, Price = ? WHERE ProductID = ?",
                   (product.ProductName, product.Category, product.Price, product.ProductID))
    conn.commit()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Product not found")
    conn.close()
    return {"message": "Product updated successfully"}

@app.delete("/products/{product_id}")
def delete_product(product_id: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE ProductID = ?",(product_id,))
    conn.commit()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Product not found")
    conn.close()
    return {"message": "Product deleted successfully"}


#Customers Endpoints
@app.get("/customers")
def get_customers():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers")
    rows= cursor.fetchall()
    conn.close()
    return rows

@app.post("/customers")
def add_customer(customer: Customer):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO customers VALUES (?,?,?,?)",
                       (customer.CustomerID, customer.Name, customer.Email, customer.Country))
        conn.commit()
        return{"message": "Customer added successfully"}
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="Customer ID already exists")
    finally:
        conn.close()

@app.put("/customers/{customer_id}")
def update_customer(customer_id: str,customer: Customer):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE customers SET Name = ?, Email = ?, Country = ? WHERE CustomerID = ?",
                   (customer.Name, customer.Email, customer.Country, customer_id))
    conn.commit()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Customer not found")
    conn.close()
    return {"message": "Customer updated successfully"}

@app.delete("/customers/{customer_id}")
def delete_customer(customer_id: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM customers WHERE CustomerID = ?",(customer_id,))
    conn.commit()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Customer not found")
    conn.close()
    return {"message": "Customer deleted successfully"}






