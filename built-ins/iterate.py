for builtin in sorted(dir(__builtins__), key = lambda w: w.upper()):

    builtin_Obj = getattr(__builtins__, builtin)
    print('{:20s}: {}'.format(builtin, type(builtin_Obj)))
