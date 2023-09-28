import time


# Функция открытия реле
def open_relay(ser):
    ser.write(b'\x01')


# Функция закрытия реле
def close_relay(ser):
    ser.write(b'\x00')


# Функция проверки штрих-кода
def check_barcode(ser):
    barcode_file_path = 'barcode.txt'
    universal_code = '2102062129298'
    max_scans = 3
    barcode_count = {}

    ser.write(b'\x50')
    time.sleep(0.1)
    if ser.in_waiting:
        i = ser.read()
        if i == b'\xAD':
            print("ICSE013A 2-Channel")
        elif i == b'\xAB':
            print("ICSE012A 4-Channel")
        elif i == b'\xAC':
            print("ICSE014A 8-Channel")
        else:
            print("ERROR")

    ser.write(b'\x51')
    time.sleep(0.5)
    ser.write(b'\x00')

    while True:
        # Запрос ввода данных с терминала
        code = input()
        if not code:
            print("Incorrect input")
        elif code == universal_code:
            print("Universal code accepted")
            open_relay(ser)
            time.sleep(1)
            close_relay(ser)
        else:
            with open(barcode_file_path, 'r') as f:
                if code in f.read():
                    print("Barcode is correct")
                    barcode_count[code] = barcode_count.get(code, 0) + 1
                    if barcode_count[code] == max_scans:
                        with open(barcode_file_path, 'r') as f:
                            barcodes = f.readlines()
                        with open(barcode_file_path, 'w') as f:
                            for barcode in barcodes:
                                if barcode.strip() != code:
                                    f.write(barcode)
                        del barcode_count[code]
                    open_relay(ser)
                    time.sleep(1)
                    close_relay(ser)
                else:
                    print("Barcode is incorrect")

        time.sleep(3)  # Проверка каждые 3 секунды
