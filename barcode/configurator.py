# configurator.py

import configparser


def load_settings():
    config = configparser.ConfigParser()
    config.read('settings.txt')
    output_paths = config['Paths'].values()
    return output_paths
