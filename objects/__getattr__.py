#!/usr/bin/python3

#
# Useful to access members of a dictionary with a dot:
#    https://stackoverflow.com/questions/2352181/how-to-use-a-dot-to-access-members-of-dictionary
#

class C:

    def __init__(self):
        self.member_one = 1
        self.member_two = 2

    def __getattr__(self, name):
        print('C.__getattr__ with name = ' + name + ' was called')

    def method_one(self):
        print('method_one was called')


c = C()

print(str(c.member_one  ))
print(str(c.member_two  ))
print(str(c.member_three))

c.method_one()
c.method_two()
