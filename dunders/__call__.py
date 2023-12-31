import types

class C(): pass

def   f(): pass


if callable(C): print('C is callable')
if callable(f): print('f is callable')

if C.__class__ is types.FunctionType: print('C.__class__ is types.FunctionType')
if f.__class__ is types.FunctionType: print('f.__class__ is types.FunctionType')

# if C.__code__  is types.CodeType    : print('C.__code__ is types.CodeType')
if f.__code__  is types.CodeType    : print('f.__code__ is types.CodeType')
