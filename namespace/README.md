Most namespaces are currently implemented as Python dictionaries

Namespaces are created at different moments and have different lifetimes. The namespace containing the built-in names is created when the Python interpreter starts up,

The built-in names actually also live in a module; this is called builtins.

The local namespace for a function is created when the function is called, and deleted when the function returns or raises an exception that is not handled within the function
