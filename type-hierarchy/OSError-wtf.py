for builtin in dir(__builtins__):

    builtin_ = getattr(__builtins__, builtin)
#   print(builtin)

    if (issubclass(type(builtin_), type)):
        type_name = builtin_.__name__
        
        if type_name == 'OSError':
           print(type_name)
           print(builtin_)
           print(builtin)
    

           print()


print(OSError.__name__         )
print(EnvironmentError.__name__)
print(repr(OSError))
print(repr(EnvironmentError))

print(id(OSError         ))
print(id(EnvironmentError))
print(id(IOError         ))
print(id(WindowsError    ))

if OSError is EnvironmentError is IOError is WindowsError:
   print('Yes, the same')
