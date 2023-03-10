#!/usr/bin/env python

import pandas
import pickle

# tab = {
#    'col 1': ['one', 'two', 'three'],
#    'col 2': [   1 ,    2 ,      3 ],
#    'col 3': ['foo', 'bar', 'baz'  ],
# }
# 
# with open('obj.pickled', 'wb') as f:
#     pickle.dump(tab, f)
# 
# df = pandas.read_pickle('obj.pickled')
# 
# print(df)

# import pandas as pd
# import pickle
# 
# # Create a sample object to serialize
# my_object = {'name': 'John', 'age': 30, 'location': 'New York'}
# 
# # Dump the object to a pickled file
# with open('example.pkl', 'wb') as file:
#     pickle.dump(my_object, file)
# 
# # Load the pickled file into a DataFrame
# df = pd.read_pickle('example.pkl')
# 
# # Print the DataFrame
# print(df)



import pandas as pd
import pickle

# Create a sample DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})

# Dump the DataFrame to a pickled file
with open('example.pkl', 'wb') as file:
    pickle.dump(df, file)

# Read the pickled file into a new DataFrame
# new_df = pd.read_pickle('example.pkl')

new_df = pickle.load(open('example.pkl', 'rb'))

# Display the new DataFrame
print(new_df)
