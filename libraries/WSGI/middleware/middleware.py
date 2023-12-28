import textWithUmlauts

class addContentLength:

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):

        appStatus  = None
        appHeaders = []
        appExcInfo = None

        def start_response_callback(status, headers, exc_info=None):

            nonlocal appStatus, appHeaders, appExcInfo

            appStatus  = status
            appHeaders = headers
            appExcInfo = exc_info

        appBody = self.app(environ, start_response_callback)

        body  = (b''.join(appBody)).decode('utf-8')
        body += '\nThis line was added by the middleware "addContentLength"'  # 57 bytes (+108 = 165)

        bodyBytes = body.encode('utf-8')

      # Remove the Content-Length header if provided by the wrapped application 
        headers = [ (k, v) for k, v in appHeaders if k.lower() != 'content-length' ]

      # Calculate and add Content-Length
        headers.append( ('Content-Length', str(len(bodyBytes)) ) )

        start_response(appStatus, headers, appExcInfo)
        return [bodyBytes]

application = addContentLength(textWithUmlauts.application)
