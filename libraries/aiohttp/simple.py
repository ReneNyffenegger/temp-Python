from aiohttp import web
# import logging


async def hello(request):
#
#   A request handler must be
#      a coroutine that
#      accepts a Request instance as its only argument and
#      returns a StreamResponse derived (e.g. Response)instance:
#
    return web.Response(text='Hello, world\n')

async def post(request):
    return web.Response(text='''this body is
returned as result of
the /post request''')

app = web.Application()

# app.logger.setLevel(logging.DEBUG)
# app.logger.addHandler(logging.StreamHandler())
# app.logger.debug('server.log')

app.add_routes([
   web.get ('/'    , hello),
   web.post('/', post )
])

web.run_app(app, port=8427)
