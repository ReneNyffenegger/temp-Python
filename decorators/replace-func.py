#!/usr/bin/python3


def alternativeFunc():
    print("The alternative function was called.")

def ReplaceFunc(func):
    return alternativeFunc


@ReplaceFunc
def justAFunc():
    print('just a func')

justAFunc()
# The alternative function was called
