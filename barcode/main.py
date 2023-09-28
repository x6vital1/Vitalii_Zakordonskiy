# main.py

import configparser
import threading
import time
import serial
import logging
from barcode_checker import check_barcode
from barcode_generator import generate_barcode
from logger import setup_logging
from com_port_finder import find_com_port

vendor_id = 0x067B  # Замените на соответствующий вендор-идентификатор
product_id = 0x2303  # Замените на соответствующий продукт-идентификатор

# Загрузка настроек из файла settings.txt
config = configparser.ConfigParser()
config.read('settings.txt')
output_paths = config['Paths'].values()


# Запуск функций
def main():
    setup_logging()
    com_port = find_com_port(vendor_id, product_id)
    if com_port is None:
        logging.error("USB-устройство не найдено.")
        exit()

    ser = serial.Serial(com_port, 9600, timeout=0.1)
    time.sleep(0.1)

    barcode_thread = threading.Thread(target=check_barcode, args=(ser,))
    barcode_thread.start()

    generate_barcode()

    ser.close()


if __name__ == "__main__":
    main()
