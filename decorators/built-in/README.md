
    @decoratorFunc
    def func(*args, **kwargs)
        pass

translates to

    func = decoratorFunc(foo)

# Built-in decorators:

    @staticmethod
    @classmethod
    @property           (used for getters and setters)
