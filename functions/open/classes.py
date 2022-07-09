w_ = open('w_', 'w' )
wb = open('wb', 'wb')

def cls(obj):
#   print('{:40s} {:s}'.format(str(type(type(obj))), str(type(obj).mro())))
    obj_t = type(obj)
#   print('{:40s} {:s}'.format('.'.join([obj_t.__module__, obj_t.__qualname__]), str(type(obj).mro())))
    print('{:40s} {:s}'.format(
       '.'.join([obj_t.__module__, obj_t.__qualname__]),
       ' <- '.join( map(lambda t: str(t.__qualname__), type(obj).mro())
    )))


cls(w_)
cls(wb)

# print(w_.__class__)
# print(wb.__class__)
# 
# print(w_.mro())
