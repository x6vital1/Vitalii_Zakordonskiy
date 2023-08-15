import serial
import time
import serial.tools.list_ports
import datetime

vendor_id = '16c0'
product_id = '05df'
barcode_file_path = 'barcode.txt'
universal_code = '2102062129298'
max_scans = 3


# функция проверки штрих-кода
def check_barcode():
    barcode_count = {}
    while True:
        try:
            # поиск порта устройства по Vendor ID и Product ID
            ports = serial.tools.list_ports.grep(f'{vendor_id}:{product_id}')
            port = next(ports).device
            # управление реле
            ser = serial.Serial(port, 9600, timeout=1)
            time.sleep(5)
            # получение названия устройства с указанным вендор и продукт ид
            device_name = ser.name
            print(f"Device found: {device_name}")
            ser.write(bytes([0x51]))
            time.sleep(0.5)
            ser.write(bytes([0b00000000]))
            while True:
                # запрос ввода данных с терминала
                code = input()
                if code == universal_code:
                    print(f"{datetime.datetime.now().strftime('%H:%M:%S')} Universal code accepted")
                    ser.write(bytes([0b00000001]))
                    time.sleep(1)  # задержка на 1 секунду
                    # включаем первый канал реле
                    ser.write(bytes([0b00000000]))
                else:
                    with open(barcode_file_path, 'r') as f:
                        if code in f.read():
                            print(f"{datetime.datetime.now().strftime('%H:%M:%S')} Barcode is correct")
                            barcode_count[code] = barcode_count.get(code, 0) + 1
                            if barcode_count[code] == max_scans:
                                with open(barcode_file_path, 'r') as f:
                                    barcodes = f.readlines()
                                with open(barcode_file_path, 'w') as f:
                                    for barcode in barcodes:
                                        if barcode.strip() != code:
                                            f.write(barcode)
                                del barcode_count[code]
                            ser.write(bytes([0b00000001]))
                            time.sleep(1)  # задержка на 1 секунду
                            # выключаем первый канал реле
                            ser.write(bytes([0b00000000]))
                        else:
                            print(f"{datetime.datetime.now().strftime('%H:%M:%S')} Barcode is incorrect")

                time.sleep(3)  # проверка каждые 3 секунды
            ser.close()
        except StopIteration:
            print(f"Device not found, trying again in 5 seconds")
            time.sleep(5)


# запуск функции в фоновом режиме
check_barcode()
