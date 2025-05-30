#!/usr/bin/env python3
#
#      TODO: Use (deprecated) cgi module to parse uploaded file.
#
#   https://stackoverflow.com/a/52234729/180275
#   
#
# Reflects the requests with dummy responses from HTTP methods GET, POST, PUT, and DELETE
# Written by Tushar Dwivedi (2017)

#
#
#

from http.server import BaseHTTPRequestHandler, HTTPServer

# from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler


class tq84HttpServer(BaseHTTPRequestHandler):

    @staticmethod
    def slash():
         return bytes('''
     <!DOCTYPE html>
     <html>
     <head>
        <meta charset="UTF-8">
        <title>Hello</title>
     </head>
     <body>
       <h1>Hello</h1>
       Some stränge charactérs, ĵust før fun.

       <p>

       <form action="/upload" method="post" 
             enctype="multipart/form-data"
       >
    <!--    
             enctype="application/x-www-form-urlencoded"
             enctype="text/plain"
             -->
           <label for="fileUpload">Choose a file to upload:</label>
           <input type="file" id="fileUpload" name="fileUpload">
           <input type="submit" value="Upload File">
       </form>

       <p><a href='enter-text'>Enter text</a>

     </body>
     </html>''', 'utf-8')

    def enter_text(self, content = ''):

#       print('a')
#       print(type(self.rfile))
#       print('b')
#       print(self.rfile.readable())
#       print('b2')
#       content = self.rfile.read(-1)
#       print(f'c: {content}')
#       content = self.rfile.readlines()

#       for x in dir(self.rfile):
#           print(x)
        
        title = 'Enter text'
        return bytes(f'''
     <!DOCTYPE html>
     <html>
     <head>
        <meta charset="UTF-8">
        <title>{title}</title>
     </head>
     <body>
       <h1>{title}</h1>

       <form action="/enter-text" method="post" enctype="application/x-www-form-urlencoded">
        <label for="text">Enter your text:</label><br>
        <textarea name="text" rows="20" cols="50">{content}</textarea><br><br>
        <input type="submit" value="Go!">
    </form>
     </body>
     </html>

       ''', 'utf-8')


    def response(self, content_type, body_bytes): 
#       body_encoded = bytes(body, 'utf8')

        self.send_response(200)
        self.send_header('Content-Type'  , content_type)
        self.send_header('Content-Length', str(len(body_bytes)))
        self.end_headers()

        self.wfile.write(body_bytes)

    def do_GET(self):

        if   self.path == '/':
             self.response('text/html', self.slash())

        elif self.path == '/enter-text':
             self.response('text/html', self.enter_text())


    def do_POST(self):

        content_length = int(self.headers['content-length'])
        # length = int(content_length[0]) if content_length else 0
        content = self.rfile.read(content_length) # read() returns a bytes() object

        print(f'do Post, path = {self.path}')
        if self.path == '/upload':
#          self.response('text/plain', str(type(self.headers)))
#          print(self.headers['content-length'])
           print(f'type(self.headers) = f{str(type(self.headers))}')

#          print('self.headers.keys')
#          for x in dir(self.headers.keys()):
#              print(x)
#          print('-----------------')

           self.response('text/plain', content)

        elif self.path == '/enter-text':
           self.response('text/html', self.enter_text(content))

        # print("length :", length)

        # print("<----- Request End -----\n")

#       self.send_response(200)
#       self.send_header("Set-Cookie", "foo=bar")
#       self.end_headers()
#       self.wfile.write(json.dumps({'hello': 'world', 'received': 'ok'}))

    do_PUT    = do_POST
    do_DELETE = do_GET


# def main():
#     port = 8082
#     print('Listening on localhost:%s' % port)
#     server = HTTPServer(('', port), RequestHandler)
#     server.serve_forever()


#if __name__ == "__main__":
#    parser = OptionParser()
#    parser.usage = ("Creates an http-server that will echo out any GET or POST parameters, and respond with dummy data\n"
#                    "Run:\n\n")
#    (options, args) = parser.parse_args()
#
#    main()


server = HTTPServer( ('', 8888),  tq84HttpServer )
server.serve_forever()
