# barcode_generator.py

import datetime
import os
import configparser
import pathlib
import logging
import random
import time
import sys

from barcode import Code128
from barcode.writer import ImageWriter
from logger import setup_logging

config = configparser.ConfigParser()
config.read('settings.txt')
output_paths = config['Paths'].values()

BARCODE_FILE = 'barcode.txt'
LOGOTIP_FILENAME = 'Logotip'

last_clear_time = datetime.datetime.now()
last_checked_time = datetime.datetime.now()
project_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
logotip_path = os.path.join(project_dir, LOGOTIP_FILENAME)


def generate_barcode():
    setup_logging()
    global last_clear_time, last_checked_time
    while True:
        try:
            # проверяем, прошло ли с последней очистки файла более 24 часов
            if (datetime.datetime.now() - last_clear_time).total_seconds() >= 24 * 60 * 60:
                open(BARCODE_FILE, 'w').close()  # очистка файла
                last_clear_time = datetime.datetime.now()  # обновляем время последней очистки

            # проверяем, прошло ли с последней проверки времени более 5 минут
            if (datetime.datetime.now() - last_checked_time).total_seconds() >= 5 * 60:
                # проверяем, текущее время больше или равно 8:00 утра и еще не было очистки сегодня
                if datetime.datetime.now().time() >= datetime.time(8,
                                                                   0) and datetime.datetime.now().date() > last_clear_time.date():
                    open(BARCODE_FILE, 'w').close()  # очистка файла
                    last_clear_time = datetime.datetime.now()  # обновляем время последней очистки

                last_checked_time = datetime.datetime.now()  # обновляем время последней проверки времени

            # генерация штрих-кода
            ean = Code128(str(random.randint(100000000000, 999999999999)), writer=ImageWriter())
            ean.save('Logotip', options={"format": "bmp", "module_width": 0.5, "module_height": 20})
            logging.info(f"Generated barcode: {ean}")
            with open(BARCODE_FILE, 'a') as f:
                f.write(f'{ean.get_fullcode()}\n')
            try_count = 0
            for output_path in output_paths:
                try:
                    src = pathlib.Path('Logotip.bmp')
                    dst = pathlib.Path(output_path) / 'Logotip.bmp'
                    dst.write_bytes(src.read_bytes())  # Копирование файла
                except FileNotFoundError:
                    logging.info(f"Folder not found: {output_path}. Retrying in 10 seconds... ({try_count})")
                    try_count += 1
                    if try_count > 10:
                        logging.info(f"Failed to copy barcode file to {output_path}. Skipping this iteration.")
                        break
                    time.sleep(10)
                except Exception as e:
                    logging.info(f"Error occurred while copying file to {output_path}: {str(e)}")
        except Exception as ex:
            logging.info(f"An error occurred: {str(ex)}")

        time.sleep(15)
