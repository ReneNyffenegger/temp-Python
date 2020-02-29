import sys

# types = [
#   { 'name':  'list'      , 'instance': [] },
#   { 'name':  'tuple'     , 'instance': () },
#   { 'name':  'dict'      , 'instance': {} },
#   { 'name':  'string'    , 'instance': '' },
#   { 'name':  'dict_items', 'instance': {}.items() },
# ]


types = [
  { 'instance': []               },
  { 'instance': ()               },
  { 'instance': {}               },
  { 'instance': ''               },
  { 'instance': 42               },
  { 'instance': 9.9              },
  { 'instance': complex(0,0)     },
  { 'instance': {}.items()       },
  { 'instance': map   (None, []) },
  { 'instance': filter(None, []) },
  { 'instance': lambda x: x      },
  { 'instance': open('dummy','w')},
]

types_with_attribute = {}

for T in types:
    T['type'] = type(T['instance'])
    T['name'] = T['type'].__name__
#   print("{:15}: {:}".format( (T['name']), str(type(T['instance'])))  )
#   print(T['name'])

    T['attributes'] = []
    for A in dir(T['instance']):

        if not A in types_with_attribute:
           types_with_attribute[A] = {'cnt': 0, 'seen_in': {}}

        types_with_attribute[A]['cnt'    ] += 1
 #      types_with_attribute[A][T['name']]['cnt'] += 1
        types_with_attribute[A]['seen_in'][T['name']] = 1
#       types_with_attribute[A][T['name']] = 'seen'


html = open('attributes-in-types.html', 'w')

html.write('<!DOCTYPE html>\n<html><head><title>Attributes in types</title></head><body>')

html.write('<h1>Matrix of types and their attributes (Python version {}.{})</h1>'.format( sys.version_info.major, sys.version_info.minor))

html.write('<table border=1>')

# print(type(html))

html.write('<tr><td></td><td>')
# print("\t", end='') # end='' prevents printing of newline

html.write('</td><td>'.join(types_with_attribute.keys()))
# print("\t".join(types_with_attribute.keys()))
html.write('</td></tr>')
for T in types:

#   print(T['name'], end='')

    html.write('<tr><td>')
    html.write(T['name'])
    html.write('</td>')
    for A in types_with_attribute:
#       print("\t", end='')
        html.write('<td>')

        if T['name'] in types_with_attribute[A]['seen_in']:
           html.write('x')
        else:
           html.write('')

        html.write('</td>')

    html.write('</tr>')


html.write('</body></html>')
html.close()

#   for attr in dir(type_['instance']):
#       attrs[type_['name']].append(attr)
#       print(attr)


#   print(type(type_['instance']))
#   print("{%0:<10} {%1}".format(type(typ['name']), type(typ['instance'])))


# lst = []
# tup = ()
# dct = {}
# str = ''
# 
# print(type( lst ))
# #
# #  <class 'list'>
# 
# print(type( tup ))
# #
# #  <class 'tuple'>
# 
# print(type( dct ))
# #
# #  <class 'dict'>
# 
# 
# print(type( str ))
# #
# #  <class 'str'>
# 
# 
# print("\t".join(dir(lst)))
# print("\t".join(dir(tup)))
# print("\t".join(dir(dct)))
# print("\t".join(dir(str)))
