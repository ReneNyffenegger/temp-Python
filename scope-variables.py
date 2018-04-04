var_1='foo'
var_2='FOO'

def print_var():
    var_1='bar'
    global var_2
    var_2='BAR'
    print(var_1) # bar
    print(var_2) # BAR

print_var()
print(var_1) # foo
print(var_2) # BAR



for i in range(1, 4):

    if i == 3:
    #  Access variable that is »declared« further below
       print(x) # 2

    x=i
