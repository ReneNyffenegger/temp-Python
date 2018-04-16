g_one = 42
g_two = 99

def G():
  #
  # This function has no assignment to g_one,
  # therefore, this variable is recognized as global.
  #
    v = g_one
    v = v+1
    print('v = {:d}'.format(v))
  #
  # However, there is an assignement to g_two,
  # the variable is falsely assumed to be local!
  #
    try:
      print(g_two)
      g_two += 1
    except UnboundLocalError as e:
      print(str(e))

G()
