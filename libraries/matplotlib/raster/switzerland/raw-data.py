
#
#                 2                   4                   6                   8                           
# 2 3 4 5|6 7 8 9 0|1 2 3 4 5|6 7 8 9 0|1 2 3 4 5|6 7 8 9 0|1 2 3 4 5|6 7 8 9 0|1 2 3 4 5|6 7 8 9 0|1 2 3 4 5|6 7 8 9 0|1 2 3 4 5|6 7 8 9 0|1 2 3 4 5|6 7 8 9 0|
pixels = '''
                                                                               |x x
                                                                              x|x x x
                                                                            x x|x x x   x|
                                                                            x x|x x x x x|x   x x  |
                                                                               +---------+---------+
                                                                                  x x x x|x x x x x|x x
                                                 |x x     x|x       x|x x     x|  x x x x|x x x x x|x x x
                                                x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x
                             |  x x x x|      x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x
                             |  x x x x|      x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x
                             +---------+---------+---------+---------+---------+---------+---------+---------+--------
                             |x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x
                             |x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x
                             |    x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x
                             |  x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x 
                             |x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x 
                             +---------+---------+---------+---------+---------+---------+---------+---------+--------
                            x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x
                          x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x
                        x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x
                        x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x
                      x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x        |      x x|
                   +---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+
                  x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x        |      x x|
                x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x    |  x x x x|x
                x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x  |  x x x x|x
                x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|
                x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|
                ---+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+----
              x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|
         |x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x  |
        x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x
      x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|    x x x|x
      x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|      x x|x
         +---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+----
    x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x  |
    x x x|x x x    |    x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x x x x|x x   x  |x x x x x|x x x x  |
    x x x|x        |        x|x x x x x|x x x x x|x x x x x|x x x x x|x x x   x|x x x x x|x x x x x|x x     x|x x x x x|x x x x x|x
      x x|         |      x x|x x x x x|x x x x x|x x x x x|x x x x x|x x     x|x x x x x|x x x x x|x x      |x x x x x|      x x|x
      x  |         |    x x x|x x x x x|x x x x x|x x x x x|x x x x x|x       x|x x x x x|x x x x x|x x x    |x x x x x|      x x|
   ----- +---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+----
    x x  |         |      x x|x x x x x|x x x x x|x x x x x|x x x x x|x       x|x x x x x|x x x x x|x x      |  x x x  |      x x|x
  x x   x|x        |        x|x x x x x|x x x x x|x x x x x|x x x x  |        x|x x x x x|x x x x x|x x      |         |        x|x
x x x x x|         |      x x|x x x x x|x x x x x|x x x x x|x x x x x|        x|x x x x x|x x x x x|x        |         |        x| 
x x x x  |         |      x x|x x x x x|x x x x x|x x x x x|x x x x x|        x|x x x x x|x x x x x|x        |         |         | 
                          x x|x x x x x|x x x x x|x x x x x|x x x x x|         |  x x x x|x x x x x|         |           
   ----- +---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+----
                            x|x x x x x|x x x x x|x x x x x|x x x    |         |    x   x|x x x x  |         |           
                            x|x x x x x|x x x x x|x x x x x|x x x    |         |         |x x x    |         |           
                             |  x x x x|x x x x x|x x x x x|x x      |         |        x|x x x x  |         |           
                             |    x x x|x x x x x|    x x x|x x      |         |         |x x x    |         |           
                             |    x x x|x x x    |      x x|                             |  x x x  |         |           
   ----- +---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+----
                             |      x  |         |         |                             |  x x x  |         |           
                             |         |         |         |                             |    x x  |         |           
'''


lines = [_.replace('|', ' ') for _ in pixels.splitlines() if not '-' in _ ];
print('\n'.join(lines))
