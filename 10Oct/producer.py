import pika
import json

# Step 1: Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

# Step 2: Create a queue
channel.queue_declare(queue="student_tasks")

# Step 3: Prepare a message
task = {
    "student_id": 101,
    "action": "generate_certificate",
    "email": "rahul@example.com"
}

# Step 4: Publish the message to the queue
channel.basic_publish(
    exchange="",
    routing_key="student_tasks",
    body=json.dumps(task)
)

print("Task sent to queue:", task)

# Close the connection
connection.close()