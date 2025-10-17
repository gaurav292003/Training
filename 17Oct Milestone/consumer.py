import pika
import json
import pandas as pd
import logging
from datetime import datetime

#  Configure logging
logging.basicConfig(filename='order_processing.log', level=logging.INFO,
                   format='%(asctime)s - %(message)s')

# Load products and customers CSV
products = pd.read_csv(r"C:\Users\user1\PycharmProjects\MilestoneProject\data\products.csv")
customers = pd.read_csv(r"C:\Users\user1\PycharmProjects\MilestoneProject\data\customers.csv")

#  Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='orders_queue')

# Function to process each order
def process_order(ch, method, properties, body):
   order = json.loads(body)
   # Get product and customer info
   try:
       product = products[products["ProductID"] == order["ProductID"]].iloc[0]
       customer = customers[customers["CustomerID"] == order["CustomerID"]].iloc[0]
   except IndexError:
       logging.error(f"Invalid ProductID or CustomerID for order {order['OrderID']}")
       ch.basic_ack(delivery_tag=method.delivery_tag)
       return


   # Calculate total price and order month
   total_price = order["Quantity"] * product["Price"]
   order_date = pd.to_datetime(order["OrderDate"])
   order_month = order_date.month


   # Prepare processed order record
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

   # Append to processed_orders.csv
   try:
       df = pd.read_csv("processed_orders.csv")
       df = pd.concat([df, pd.DataFrame([processed_order])], ignore_index=True)
   except FileNotFoundError:
       df = pd.DataFrame([processed_order])
   df.to_csv("processed_orders.csv", index=False)


   # Log the processed order
   logging.info(f"Processed order {order['OrderID']} for customer {order['CustomerID']}")
   print(f"Processed order {order['OrderID']}")


   # Acknowledge message
   ch.basic_ack(delivery_tag=method.delivery_tag)

   
#  Start consuming
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='orders_queue', on_message_callback=process_order)
print("Waiting for orders. Press CTRL+C to exit.")
channel.start_consuming()