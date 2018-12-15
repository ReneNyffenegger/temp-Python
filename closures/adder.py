#!/usr/bin/python3
#
# https://pymbook.readthedocs.io/en/latest/igd.html
#


# Closures are nothing but functions that are returned by another function. 


def add_number(num):
    def adder(number):
        'adder is a closure'
        return num + number
    return adder

a_10 = add_number(10)

print(a_10(21)) # 31
print(a_10(34)) # 44

a_5 = add_number(5)

print(a_5(3)) # 8
