import csv
import logging

# Setup logging
logging.basicConfig(filename='sales.log', level=logging.INFO, format='%(levelname)s - %(message)s')

try:
    with open('sales.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            product = row['product']
            try:
                price = float(row['price'])
                quantity = int(row['quantity'])
                total = int(price * quantity)
                print(f"{product} total = {total}")
                logging.info(f"{product} total sales = {total}")
            except ValueError:
                print(f"ERROR - Invalid numeric value for product: {product}")
                logging.error(f"Invalid numeric value for product: {product}")

except FileNotFoundError:
    print("ERROR - sales.csv not found.")
    logging.error("sales.csv not found.")
