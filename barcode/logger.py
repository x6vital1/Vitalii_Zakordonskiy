# logger.py
import logging


def setup_logging():
    logging.basicConfig(filename='log.txt', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%H:%M:%S')
