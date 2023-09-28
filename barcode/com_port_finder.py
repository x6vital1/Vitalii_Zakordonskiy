# com_port_finder.py

import serial.tools.list_ports


def find_com_port(ven_id, prod_id):
    com_ports = list(serial.tools.list_ports.comports())
    for port in com_ports:
        if port.vid == ven_id and port.pid == prod_id:
            return port.device
    return None
