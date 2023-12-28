def application(environ, start_response):

    start_response(
         '200 OK',
        [('Content-Type', 'text/plain; charset=utf-8')
    ])

    return ['The total length, in bytes, of this text, '     .encode('utf-8'),
            'when encoded in UTF-8, with the three letters ' .encode('utf-8'),
            'Ä, Ö and Ü is 108'                              .encode('utf-8') ]
