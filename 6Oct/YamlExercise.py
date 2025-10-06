import yaml
import logging

# Setup logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(levelname)s - %(message)s')

try:
    # Try reading the YAML config file
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)

    # Extract database info
    db_config = config['database']
    host = db_config['host']
    port = db_config['port']
    user = db_config['user']

    # Print and log the connection string
    connection_msg = f"Connecting to {host}:{port} as {user}"
    print(connection_msg)
    logging.info("Config loaded successfully.")

except FileNotFoundError:
    error_msg = "config.yaml not found."
    print(f"ERROR - {error_msg}")
    logging.error(error_msg)
