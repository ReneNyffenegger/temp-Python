#!/usr/bin/python3

def F_outer():

    def F_inner():
        print('F_inner')

    print('F_outer')
    F_inner()

F_outer()

# 'function' object has no attribute 'F_inner'
# F_outer.F_inner()

# F_outer['<locals>'].F_inner()
