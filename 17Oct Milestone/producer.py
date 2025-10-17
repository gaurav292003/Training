import pika
import json
#Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

#Declare a queue
channel.queue_declare(queue='orders_queue')
#Sample new orders to push
new_orders = [
   {"OrderID": "0005", "CustomerID": "C001", "ProductID": "P104", "Quantity": 2, "OrderDate": "2025-10-05"},
   {"OrderID": "0006", "CustomerID": "C002", "ProductID": "P102", "Quantity": 3, "OrderDate": "2025-10-06"}
]

#Push orders to the queue
for order in new_orders:
   channel.basic_publish(
       exchange='',
       routing_key='orders_queue',
       body=json.dumps(order)
   )
   print(f" Order {order['OrderID']} pushed to queue")

# Close connection
connection.close()