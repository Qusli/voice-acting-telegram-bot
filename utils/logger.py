import os;
import logging;

class Logger:
    def __init__(self):
        if (not(os.path.exists("logs"))): 
            os.mkdir("logs")

        logging.basicConfig(filename="logs/success.log", level=logging.INFO, encoding="utf-8")

    def log(self, data):
        logging.info(data)
