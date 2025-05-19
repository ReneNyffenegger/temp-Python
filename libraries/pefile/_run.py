#!/usr/bin/env python3

import pefile

from pathlib import Path

def print_exports(pe):
    for entry in pe.DIRECTORY_ENTRY_EXPORT.symbols:
        print('  ' + entry.name.decode('utf-8'))

if False:
 # directory = Path('shobj')
 directory = Path('IDM')
 for dll_file in directory.rglob('*.dll'):

    print(dll_file)
    pe = pefile.PE(dll_file)
    print_exports(pe)


pe = pefile.PE('IDM/sfl400as.dll')
print_exports(pe)
