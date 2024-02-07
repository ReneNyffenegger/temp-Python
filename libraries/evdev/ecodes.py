from evdev import ecodes

#print(dir(ecodes))
# print(dir(ecodes.ABS))
#print(str(ecodes.KEY[42]))

for ecode in dir(ecodes):
    print(ecode + ': ' + str(type(getattr(ecodes, ecode))))
