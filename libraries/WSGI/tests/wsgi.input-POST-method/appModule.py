def application(environ, start_response):

    if environ['PATH_INFO'] == '/':

       start_response( '200 OK', [('Content-Type', 'text/html; charset=utf-8')])

       return ['''
         <h1>Create POST request with some data</h1>
         <form action="/post-request" method="post">
           Text one: <input type="text" name="text-one" value="Héllo"><br>
           Text two: <input type="text" name="text-two" value="Wörld"><p>
           <input type="submit" value="Go!">
         </form>
        '''.encode('utf-8')]


    elif environ['REQUEST_METHOD'] == 'POST':

       start_response( '200 OK', [('Content-Type', 'text/plain; charset=utf-8')])

       return [
           f'POST request for {environ["PATH_INFO"]}, data received in body shown below.\n\n'.encode('utf-8'),
           environ['wsgi.input'].read()
       ]

    else:

       start_response( '200 OK', [('Content-Type', 'text/plain; charset=utf-8')])

       return [
         f'PATH_INFO:      {environ["PATH_INFO"     ]}\n'.encode('utf-8'),
         f'REQUEST_METHOD: {environ["REQUEST_METHOD"]}'  .encode('utf-8')
       ]
