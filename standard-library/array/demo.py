import array

A = array.array('H', # 16-bit (short) unsigned integers
    [  1,
      11,
     111,
       0,
#     -1,  # OverflowError: unsigned short is less than minimum
   65535,
#  65536,  # OverflowError: unsigned short is greater than maximum
      42
    ])

