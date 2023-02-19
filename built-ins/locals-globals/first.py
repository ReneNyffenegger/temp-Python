def f():
    x = 'x in f'

    def g():
        x = 'x in g'

        print(locals ()['x'])
        print(globals()['x'])
#       print(dir(globals()['f']))
        print(globals()['f'].__code__)

#       print(globals().keys())

    g()

# x = 'x in global scope'
# f()



def outer_function():
    x = 10

    def inner_function():
        parent_scope = globals()
        print(parent_scope.keys())
     #  parent_vars = dir(parent_scope)
     #  print('Parent scope:', parent_vars)

    inner_function()

outer_function()
