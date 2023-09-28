import sys
from cx_Freeze import setup, Executable

main_script = 'main.py'

included_modules = [
    'barcode_checker',
    'barcode_generator',
    'com_port_finder',
    'configurator',
    'logger',
]

main_executable = Executable(script=main_script, icon='icon.ico')

setup(
    name='barcode v1.0',
    version='1.0',
    description='barcode_generator',
    executables=[main_executable],
    options={
        'build_exe': {
            'packages': [],
            'includes': included_modules,
            'include_files': ['settings.txt'],
        },
    },
)