class CallableClass:
    #
    # A callable is anything that can be called. 
    #

    def __call__(self):
        print('__call__ is called')

c = CallableClass()
c()
