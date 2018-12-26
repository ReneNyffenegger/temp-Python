#!/usr/bin/python3


class CLS:

    def __init__(self, val):
        self.val = val

    @classmethod
    def CLASS_METHOD(cls):
     #
     #  A class method's first parameter is the class
     #  that it is called on.
     #  This is interesting especially if the class
     #  is inherited
     #
        print(f'CLASS_METHOD, cls.__name__ = {cls.__name__}')
        return cls(42)

    @staticmethod
    def STATICMETHOD():
     #
     #  A static method doesn't have any implicit
     #  parameters.
     #
        return 'forty-two'

class DERIV(CLS):
      pass

cls_one   = CLS(5)
deriv_one = DERIV(7)

print(f'cls_one.val = {cls_one.val}')

print(f'cls_one.STATICMETHOD():   {cls_one.STATICMETHOD()}'  )
print(f'CLS.STATICMETHOD():       {CLS.STATICMETHOD()}'      )

print(f'cls_one.CLASS_METHOD():   {cls_one.CLASS_METHOD()}'  )
print(f'CLS.CLASS_METHOD():       {CLS.CLASS_METHOD()}'      )

print(f'deriv_one.CLASS_METHOD(): {deriv_one.CLASS_METHOD()}')
print(f'DERIV.CLASS_METHOD():     {DERIV.CLASS_METHOD()}'    )
