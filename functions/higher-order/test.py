#!/usr/bin/python3

def ADD(x, y):
    return x+y

def MULT(x, y):
    return x*y

def calc(func):
    return func(4, 5)

print(calc(ADD ))
print(calc(MULT))
