#!/usr/bin/python3

#
# An ojbect without __bool__ or __len__ method
# is always true:
#
class no_bool_no_len:
    pass

always_true = no_bool_no_len()

if always_true  :
   print("It's true")    
else:
   print("Well, it's false")
