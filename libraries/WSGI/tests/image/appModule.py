def application(environ, start_response):

    if environ['PATH_INFO'] == '/file.html':

       start_response(
          '200 OK',
          [('Content-Type', 'text/html; charset=utf-8')]
       )

       return [
         f'<html><body>'       .encode('utf-8'),
         f'<h1>Image</h1>'     .encode('utf-8'),
         f'<img src="img.png">'.encode('utf-8'),
         f'</body></html>'     .encode('utf-8')
       ]

    elif environ['PATH_INFO'] == '/img.png':

       start_response(
          '200 OK',
          [('Content-Type', 'image/png')]
       )

       return [open('img.png', 'rb').read()]

    else:

       start_response(
          '200 OK',
          [('Content-Type', 'text/html; charset=utf-8')]
       )

       return [
         f'<h1>404</h1>'                     .encode('utf-8'),
         f'{environ["PATH_INFO"]} not found.'.encode('utf-8')
       ]
