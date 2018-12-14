#!/usr/bin/python3

class S(object):
    __slots__ = ['x', 'y', 'z']   # instances will have attribute __slots__ instead of __dict__
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class C(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

def check_dict_and_slots_attribute(inst):
    if hasattr(inst, '__dict__'):
        print('{:s} has attribute __dict__'.format(str(inst)))

    if hasattr(inst, '__slots__'):
        print('{:s} has attribute __slots__'.format(str(inst)))


s = S('eggs', 'why', 42)
c = C('eggs', 'why', 42)

check_dict_and_slots_attribute(s)
check_dict_and_slots_attribute(c)
