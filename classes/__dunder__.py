#!/usr/bin/python3


# dunder = double underscore methods
#
# AKA: Magic methods.
#
# __init__ might be called »dunder init«.




#            __annotations__  A dict containing annotations of parameters. The keys of the dict are the parameter names, and 'return' for the return annotation, if provided.
# class.     __bases__        The tuple of base classes of a class object.
#            __bool__
#            __call__         Used for callables.
# instance.  __class__        the class to which an instance belongs
#            __closure__      None or a tuple of cells that contain bindings for the function’s free variables. See below for information on the cell_contents attribute.
#            __code__         The code object representing the compiled function body.
#            __defaults__     A tuple containing default argument values for those arguments that have defaults, or None if no arguments have a default value
#            __delete__       Used (with __set__ and __get__) to define a descriptor object
#            __dict__         The namespace supporting arbitrary function attribut
#            __doc__          The function’s documentation string, or None if unavailable; not inherited by subclasses
#            __enter__        goes along with __exit__ to define a context manager (used in with statements)
#            __eq__           Needed (with __hash__) for keys in a dictionary
#            __exit__         goes along with __enter__ to define a context manager (used in with statements)
#            __func__         is the function object; 
#            __get__          Used (with __set__ and __delete__) to define a descriptor object
#            __getitem__      Used for sequence semantics?
#            __globals__      A reference to the dictionary that holds the function’s global variables — the global namespace of the module in which the function was defined.
#            __hash__         Needed (with __eq__) for keys in a dictionary
#            __import__
#            __iter__         Anything that has an __iter__ method is an iterable.
#            __kwdefaults__   A dict containing defaults for keyword-only parameters.
#            __main__
#            __metaclass__    this was introduced to give the programmer some control over the semantics of the class statement. In particular it eases the transition from old-style classes (which are not covered in this tutorial) and new-style classes (simply called classes in this tutorial).
#            __module__       The name of the module the function was defined in, or None if unavailable.
# class.     __mro__          a tuple of classes that are considered when looking for base classes during method resolution.
# definition.__name__         The function's, class's, method's, descriptor's or generator's name 
#            __next__         Anthing that as an __iter__ and a __next__ method is an iterator.
#            __qualname__     The function’s qualified name
#            __self__         is the class instance object,
#            __set__          Used (with __get__ and __delete__) to define a descriptor object
#            __slots__
#            __str__  
# class.     __subclasses__
#            __unicode__
