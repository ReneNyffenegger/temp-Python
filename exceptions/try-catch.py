
class Ex_Base(BaseException):
      pass

class Ex_Deriv(Ex_Base):
      pass


try:
    raise Ex_Deriv()
except Ex_Base as e:
    print('Ex_Base caught')
except Ex_Deriv as e:
    print('Ex_Deriv caught')

try:
    raise Ex_Deriv()
except Ex_Deriv as e:          # Order of except's is important.
    print('Ex_Deriv caught')
except Ex_Base as e:
    print('Ex_Base caught')
