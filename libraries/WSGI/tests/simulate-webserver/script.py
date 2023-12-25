#!/usr/bin/python3

def simple_app(environ, start_response):

    start_response(
       '200 OK',                         # Status
       [('Content-Type', 'text/plain')]
    )

  #
  #  the application object returns an iterable yielding zero or more bytestrings:
  #
    return [
       'Hello world!\n'                .encode('utf-8'),
      f"Serving {environ['PATH_INFO']}".encode('utf-8')
    ]

def call_app(app, environ):
    status_headers = [None, None]

    def start_response(status, headers):
        status_headers[:] = [status, headers]

        def write(body_data):
          #
          # the write() callable, returned by start_response, is
          # provided only to support certain existing frameworks
          # and should not be used by new applications.
          # It is therefore left unimplemented here:
          #
            pass

        return write

    body_parts = app(environ, start_response)
    return status_headers[0], status_headers[1], b''.join(body_parts).decode()

# You can populate this with more WSGI environment variables
environ = {
                                 #
                                 #  WSGI splits the requested paths into two components:
   'SCRIPT_NAME': 'xyz.py',      #     SCRIPT_NAME is everything that was «used up getting here»
   'PATH_INFO'  : '/foo/bar/baz' #     PATH_INFO   is everything left over.
}

status, headers, body = call_app(simple_app, environ)

print('Status :', status)
print('Headers:', headers)
print(body)
