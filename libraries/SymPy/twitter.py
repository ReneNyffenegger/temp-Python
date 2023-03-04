#!/usr/bin/python3
#
# https://twitter.com/tagir_valeev/status/1631905594851434496
#

import sympy

strawberry, banana, pineapple = sympy.symbols('''
strawberry  banana, pineapple''')

print(
sympy.solve(
  strawberry / (banana     + pineapple) +
  banana     / (strawberry + pineapple) +
  pineapple  / (strawberry + banana   ) -
  4,
  strawberry, banana, pineapple
)
)
