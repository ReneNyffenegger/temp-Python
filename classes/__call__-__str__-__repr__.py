class TypeProxy:
    def __init__(self, _type):
        self._type = _type

    def __call__(self, *args, **kwargs):
        return self._type(*args, **kwargs)

    def __str__(self):
        return self._type.__name__

    def __repr__(self):
        return "TypeProxy(%s)" % (repr(self._type),)

print(str(TypeProxy(str)))
print(str(TypeProxy(type(""))))
