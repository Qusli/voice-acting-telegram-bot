import logging;

class Logger:
    def __init__(self):
        logging.basicConfig(filename="logs/app.log", level=logging.INFO, encoding="utf-8")
        logging.basicConfig(filename="logs/app.error.log", level=logging.ERROR, encoding="utf-8")

    def log(self, data):
        logging.info(data)

    def error(data):
        logging.error(data)
