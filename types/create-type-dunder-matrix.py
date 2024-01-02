data={}

async def a(): pass
coroutine=a()

types = [ [], lambda x: x, coroutine ]

def f(): pass

#
# It would have been nice if dict comprehension could have been
# used here… but type([]) does not have a __name__ attribute.
#
#    data = { typ.__name__: dir(typ) for typ in types }

data['dict'     ]=dir(type({}))
data['list'     ]=dir(type([]))
data['func'     ]=dir(type(f          ))
data['lambda'   ]=dir(type(lambda x: x))
data['coroutine']=dir(coroutine)
data['map-proxy']=dir(type.__dict__    )

#q # Extracting unique values
#q unique_values = sorted({val for values in data.values() for val in values})
#q 
#q # Initialize matrix
#q matrix = [['' for _ in data] for _ in unique_values]
#q 
#q # Fill matrix
#q for col, key in enumerate(data.keys()):
#q     for row, val in enumerate(unique_values):
#q         if val in data[key]:
#q             matrix[row][col] = 'x'
#q 
#q # Output
#q print("Keys:", list(data.keys()))
#q print("Values:", unique_values)
#q for row in matrix:
#q     print(row)
#q 
#q matrix = [['' for _ in data] for _ in unique_values]
#q 
#q # Fill matrix
#q for col, key in enumerate(data.keys()):
#q     for row, val in enumerate(unique_values):
#q         if val in data[key]:
#q             matrix[row][col] = 'x'
#q 
#q # Print with headers
#q keys = list(data.keys())
#q print("     ", '  '.join(keys))
#q for row, val in zip(matrix, unique_values):
#q     print(f"{val}  {'  '.join(row)}")
#q 

unique_values = sorted({val for values in data.values() for val in values})

# Initialize matrix
matrix = [['' for _ in data] for _ in unique_values]

# Fill matrix
for col, key in enumerate(data.keys()):
    for row, val in enumerate(unique_values):
        if val in data[key]:
            matrix[row][col] = 'x'

# Find the longest key for formatting
max_val_length = max(len(val) for val in unique_values)
max_key_length = max(len(key) for key in data.keys())

# Print with headers, aligned
keys = list(data.keys())
header_format = "{:>" + str(max_key_length) + "}"  # Right-align the header



row_format = "{:<" + str(max_val_length) + "}" + "  ".join(["{:>" + str(max_key_length) + "}" for _ in keys]) # Right-align columns
print(row_format)
#import sys
#sys.exit()

# print('{:<30}'.format(''), header_format.format(""), '  '.join(header_format.format(key) for key in keys))
print(row_format.format('', *[header_format.format(key) for key in keys]))
#print(row_formatformat(''), header_format.format(""), '  '.join(header_format.format(key) for key in keys))
for row, val in zip(matrix, unique_values):
    print(row_format.format(val, *row))


