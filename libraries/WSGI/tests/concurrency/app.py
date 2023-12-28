#
#  gunicorn --threads 10 app
#

import time
import threading
import os

def application(environ, start_response):

    start_response( '200 OK', [('Content-Type', 'text/plain; charset=utf-8') ])

    yield f'os.get_pid                    : {os.getpid()}\n'              .encode('utf-8')
    yield f'threading.get_native_id native: {threading.get_native_id()}\n'.encode('utf-8')
    yield f'threading.get_ident           : {threading.get_ident()}\n'    .encode('utf-8')
    for i in range(10):
        time.sleep(1)
        yield f'{i}\n'.encode('utf-8')
