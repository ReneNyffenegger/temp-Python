w_ = open('w_', 'w' )
wb = open('wb', 'wb')

def cls(obj):
    print('{:40s} {:s}'.format(str(type(obj)), str(type(obj).mro())))


cls(w_)
cls(wb)

# print(w_.__class__)
# print(wb.__class__)
# 
# print(w_.mro())
