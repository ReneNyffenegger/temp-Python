#
#    https://stackoverflow.com/questions/6463918
#
#    https://docs.python.org/3/py-modindex.html
#
import distutils.sysconfig as sysconfig
import os

std_lib = sysconfig.get_python_lib(standard_lib=True)

for top, dirs, files in os.walk(std_lib):
    for nm in files:
        if nm != '__init__.py' and nm[-3:] == '.py':
            print(os.path.join(top, nm)[len(std_lib)+1:-3].replace(os.sep, '.'))
