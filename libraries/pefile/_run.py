#!/usr/bin/env python3

import pefile

from pathlib import Path

def print_exports(pe):

    if not hasattr(pe, 'DIRECTORY_ENTRY_EXPORT'):
       print('PE does not have attribute DIRECTORY_ENTRY_EXPORT')
       return

    for entry in pe.DIRECTORY_ENTRY_EXPORT.symbols:
        print('  ' + entry.name.decode('utf-8'))

def print_imports(pe):
    for entry in pe.DIRECTORY_ENTRY_IMPORT:
     print(f"Imported DLL: {entry.dll.decode('utf-8')}")
     for imp in entry.imports:
      # Some imports may not have a name (imported by ordinal)
        name = imp.name.decode('utf-8') if imp.name else f"Ordinal: {imp.ordinal}"
        print(f"\t{name} at 0x{imp.address:08x}")

if False:
 # directory = Path('shobj')
 directory = Path('IDM')
 for dll_file in directory.rglob('*.dll'):

    print(dll_file)
    pe = pefile.PE(dll_file)
    print_exports(pe)


pf = 'pixannot.dll'
# pf = 'pixlocn.dll'
# pf = 'fndapp.exe'
# pf = 'fnstkynt.ocx'
# pe = pefile.PE('IDM/sfl400as.dll')
# pe = pefile.PE('IDM/wvcore.dll')
# pe = pefile.PE('IDM/devect.dll')

pe = pefile.PE(pf)
print_imports(pe)
print_exports(pe)


#if False:
# pe = pefile.PE('IDM/sfl400as.dll')
# print_exports(pe)
# print_imports(pe)
#
#pe = pefile.PE('IDM/wvcore.dll')
#print_exports(pe)
#print_imports(pe)
#
#pe = pefile.PE('IDM/devect.dll')
#print_exports(pe)
#print_imports(pe)
