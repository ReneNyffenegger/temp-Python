#!/usr/bin/python3

x='eggs'
y='hwy'
num=42
dbl=123.456789

print(f"x: {x}, y: {y}, num: {num} dbl: {dbl}")

print(f"x: {x}, y: {y}, num: {num} dbl: {dbl:.4f}")
print(f"x: {x}, y: {y}, num: {num} dbl: {dbl:7.1f}")

def Func():
    pass

print(f"name of func: {Func.__name__}")
print(f"name of func: {Func.__name__!r}")  # !r: use repr()
