sudo pip install tornado


Three main components:
  - A web framework
      (including RequestHandler which is subclassed to create web
       applications, and various supporting classes).
  - Client- and server-side implementions of HTTP (
      HTTPServer and AsyncHTTPClient).
  - An asynchronous networking library including the classes IOLoop and
    IOStream, which serve as the building blocks for the HTTP components and
    can also be used to implement other protocols.

  The Tornado web framework and HTTP server together offer a full-stack alternative to WSGI.

A Tornado web application generally consists of
  - one or more RequestHandler subclasses,
  - an Application object which routes incoming requests to handlers, and
  - a main() function to start the server.

Tornado with SSL:
   https://groups.google.com/g/python-tornado/c/3nTrpZDsNhU
