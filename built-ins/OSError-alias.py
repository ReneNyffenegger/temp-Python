for builtin in sorted(dir(__builtins__)):

    builtin_Obj = getattr(__builtins__, builtin)

    if id(builtin_Obj) == id(OSError):
       print(builtin)
