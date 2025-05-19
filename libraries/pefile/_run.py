#!/usr/bin/env python3

import pefile

from pathlib import Path

directory = Path('shobj')
for dll_file in directory.rglob('*.dll'):

    print(dll_file)
    pe = pefile.PE(dll_file)

    for entry in pe.DIRECTORY_ENTRY_EXPORT.symbols:
        print('  ' + entry.name.decode('utf-8'))
