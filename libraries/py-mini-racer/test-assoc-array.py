from py_mini_racer import MiniRacer

js = """
let v = {
   "txt": "Hello world",
   "num":  42,
   "val": [
     [1, 2, 3],
     [4, 5, 6]
    ]
};
"""

ctx = MiniRacer()
result = ctx.eval(js)
print(ctx.eval('v.val[1][2]'))
print(ctx.eval('v.txt'))
print(ctx.eval('v.num'))
