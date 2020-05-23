builtin_types = {}


def ensureTypeInDict(t, typeName):
    global builtin_types

    print(f'  ensureTypeInDict, {t.__name__}, {typeName}')

    if not id(t) in builtin_types:

       print('   missing')

       builtin_types[id(t)] = { 
           'names'   : [],          # special key to store names of aliases (for example: OSError is EnvironmentError is IOError is WindowsError)
           'children': []           # type ids of children
       }
    else:
       print('   already here')

    if not typeName in builtin_types[id(t)]['names']:
       print(f'  name {typeName} is missing, though')
       builtin_types[id(t)]['names'].append(typeName)
    

for builtin_type in [ T for T in [ getattr(__builtins__, B) for B in dir(__builtins__) ]  if issubclass(type(T), type) ]:

 #
 #  Iterate over built-in types, assigning each built-in type to builtin_type
 #

    if builtin_type is object: 
       continue

    assert len(builtin_type.__bases__) == 1

    type_name = builtin_type.__name__
    base_name = builtin_type.__bases__[0].__name__
    base_type = getattr(__builtins__, base_name)

    print('builtin_type iteration:', base_name, '->', type_name)

    ensureTypeInDict(builtin_type, type_name)
    ensureTypeInDict(base_type   , base_name)

    if not id(builtin_type) in builtin_types[id(base_type)]['children']:
       builtin_types[id(base_type)]['children'].append(id(builtin_type))

#q #   continue
#q 
#q     if not id(builtin_type) in builtin_types:
#q #      print("ADDING", base_name)
#q        builtin_types[id(type_name)] = { 
#q          'names'   : [ type_name ],          # special key to store names of aliases (for example: OSError is EnvironmentError is IOError is WindowsError)
#q          'children': []
#q        }
#q     else:
#q        builtin_types[id( type_name)].append(type_name)
#q 
#q     builtin_types[base_name]['children'].append({ type_name)
#q #   builtin_types[base_name]['children'].append({ type_name)


def printTypeChildren(typeId, indent = 0):

    print( ('  ' * indent) + (', '.join(builtin_types[typeId]['names'] )))

#   if type_name in builtin_types:
    for child_id in builtin_types[typeId]['children']:
#       print(f'child_id = {child_id}')
        
        printTypeChildren(child_id, indent+1)
        



printTypeChildren(id(object))
