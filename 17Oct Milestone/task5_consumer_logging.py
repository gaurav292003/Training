import pika
import json
import pandas as pd
import logging
from datetime import datetime
import time
# -------------------------
# Logging Configuration
# -------------------------
logging.basicConfig(
   filename='order_processing.log',
   level=logging.INFO,
   format='%(asctime)s - %(levelname)s - %(message)s'
)
# -------------------------
# Load Product & Customer Data
# -------------------------
products = pd.read_csv(r"C:\Users\user1\PycharmProjects\MilestoneProject\data\products.csv")
customers = pd.read_csv(r"C:\Users\user1\PycharmProjects\MilestoneProject\data\customers.csv")
# -------------------------
# RabbitMQ Connection
# -------------------------
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='orders_queue')
# -------------------------
# Counters for ETL
# -------------------------
orders_processed = 0
start_time = time.time()
# -------------------------
# Function to Validate Orders
# -------------------------
def validate_order(order):
   if order["Quantity"] <= 0:
       raise ValueError(f"Invalid Quantity {order['Quantity']} for Order {order['OrderID']}")
   if order["ProductID"] not in products["ProductID"].values:
       raise ValueError(f"ProductID {order['ProductID']} not found")
   if order["CustomerID"] not in customers["CustomerID"].values:
       raise ValueError(f"CustomerID {order['CustomerID']} not found")
# -------------------------
# Process Each Order
# -------------------------
def process_order(ch, method, properties, body):
   global orders_processed
   order = json.loads(body)
   logging.info(f"Order received: {order}")
   try:
       # Validate order
       validate_order(order)
       # Merge product and customer info
       product = products[products["ProductID"] == order["ProductID"]].iloc[0]
       customer = customers[customers["CustomerID"] == order["CustomerID"]].iloc[0]
       total_price = order["Quantity"] * product["Price"]
       order_month = pd.to_datetime(order["OrderDate"]).month
       processed_order = {
           "OrderID": order["OrderID"],
           "CustomerID": order["CustomerID"],
           "Name": customer["Name"],
           "Email": customer["Email"],
           "Country": customer["Country"],
           "ProductID": order["ProductID"],
           "ProductName": product["ProductName"],
           "Category": product["Category"],
           "Quantity": order["Quantity"],
           "Price": product["Price"],
           "TotalPrice": total_price,
           "OrderDate": order["OrderDate"],
           "OrderMonth": order_month
       }
       # Append to CSV
       try:
           df = pd.read_csv("processed_orders.csv")
           df = pd.concat([df, pd.DataFrame([processed_order])], ignore_index=True)
       except FileNotFoundError:
           df = pd.DataFrame([processed_order])
       df.to_csv("processed_orders.csv", index=False)
       # Logging success
       logging.info(f"Order processed and saved: {order['OrderID']}")
       orders_processed += 1
       print(f"Processed order {order['OrderID']}")
   except Exception as e:
       logging.error(f"Error processing order {order['OrderID']}: {str(e)}")
       print(f" Error: {str(e)}")
   finally:
       ch.basic_ack(delivery_tag=method.delivery_tag)
# -------------------------
# Start Consuming Orders
# -------------------------
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='orders_queue', on_message_callback=process_order)
try:
   print(" Waiting for orders. Press CTRL+C to exit.")
   channel.start_consuming()
except KeyboardInterrupt:
   end_time = time.time()
   duration = end_time - start_time
   logging.info(f"ETL finished: Processed {orders_processed} orders in {duration:.2f} seconds")
   print(f"ETL finished: Processed {orders_processed} orders in {duration:.2f} seconds")
   connection.close()