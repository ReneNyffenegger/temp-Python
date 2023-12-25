
def app(environ, start_response):

    start_response(
       '200 OK',
       [('Content-Type', 'text/plain')]
    )

  #
  #  the application object returns an iterable yielding zero or more bytestrings:
  #
    return [
       'Hello world!\n'                .encode('utf-8'),
      f"Serving {environ['PATH_INFO']}".encode('utf-8')
    ]

#from wsgiref.simple_server import make_server, demo_app
from  wsgiref.simple_server import WSGIServer , WSGIRequestHandler , demo_app

host = ''   # Localhost?
port = 1234

wsgiServer = WSGIServer( (host,port) , WSGIRequestHandler )
wsgiServer.set_app(app)
wsgiServer.serve_forever()

#
#with make_server('', 8000, demo_app) as httpd:
#    print("Serving HTTP on port 8000...")
#
#    # Respond to requests until process is killed
#    httpd.serve_forever()
#
#    # Alternative: serve one request, then exit
#    httpd.handle_request()
