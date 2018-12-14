#
# A scope is a textual region of a Python program where a namespace is directly accessible. 
# Directly accessible” here means that an unqualified reference to a name attempts to find the name in the namespace.
#
# At any time during execution, there are at least three nested scopes whose namespaces are directly accessible:
#  - the innermost scope, which is searched first, contains the local names
#  - the scopes of any enclosing functions, which are searched starting with the nearest enclosing scope, contains non-local, but also non-global names
#  - the next-to-last scope contains the current module’s global names
#  - the outermost scope (searched last) is the namespace containing built-in names
#

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
