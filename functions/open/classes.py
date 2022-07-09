w_ = open('w_'    , 'w' )
wb = open('wb'    , 'wb')
rb = open(__file__, 'rb')

def cls(obj):
#   obj_t = type(obj)
    print(' <- '.join( map(lambda t: '.'.join([t.__module__, t.__qualname__]), type(obj).mro())))
#   print('{:20s}:  {:s}'.format(
#      '.'.join([obj_t.__module__, obj_t.__qualname__]),
#      ' <- '.join( map(lambda t: '.'.join([t.__module__, t.__qualname__]), type(obj).mro())
#   )))


cls(w_)
cls(wb)
cls(rb)

# print(w_.__class__)
# print(wb.__class__)
# 
# print(w_.mro())
