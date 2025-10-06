import logging

logging.basicConfig(
    filename='app.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.debug("This is a message")
logging.info("Application started")
logging.warning("Low memory warning")
logging.error("File Not Found")
logging.critical("Critical System failure")