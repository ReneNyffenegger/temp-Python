import sys

# types = [
#   { 'name':  'list'      , 'instance': [] },
#   { 'name':  'tuple'     , 'instance': () },
#   { 'name':  'dict'      , 'instance': {} },
#   { 'name':  'string'    , 'instance': '' },
#   { 'name':  'dict_items', 'instance': {}.items() },
# ]


types = [
# { 'instance': __builtins__     },
  { 'instance': sys              },
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

html.write("<!DOCTYPE html>\n<html><head><title>Attributes in types</title></head><body>")

html.write('<h1>Matrix of types and their attributes (Python version {}.{})</h1>'.format( sys.version_info.major, sys.version_info.minor))

html.write('\n\n<table border=1>')


html.write('<tr><td></td>')

for A, v  in types_with_attribute.items():
    if v['cnt'] == len(types): continue
    if v['cnt'] == 1         : continue


    html.write('<td>{} ({})</td>'.format(A, v['cnt']))

# html.write('</td><td>'.join(types_with_attribute.keys()))


html.write('</tr>')
for T in types:


    html.write('\n<tr><td>')
    html.write(T['name'])
    html.write('</td>')
    for A, v in types_with_attribute.items():

        if v['cnt'] == len(types): continue
        if v['cnt'] == 1         : continue

        html.write('<td>')

        if T['name'] in types_with_attribute[A]['seen_in']:
           html.write('x')
#          html.write(A)
        else:
           html.write('')

        html.write('</td>')

    html.write('</tr>')
html.write('<table>')

html.write('\n<h2>Attributes that were seen in all types</h2>')
html.write('<ul>')

for A, v in types_with_attribute.items():

    if v['cnt'] == len(types):
       html.write('<li>{}'.format(A))

html.write('</ul>')


html.write('\n<h2>Attributes that were seen in one type only</h2>')

for T in types:

    html.write('<h3>{}</h3>'.format(T['name']))

    html.write('<ul>')

    for A, v in types_with_attribute.items():

        if v['cnt'] != 1: continue
        if T['name'] in v['seen_in']:
           html.write('<li>{}'.format(A))

    html.write('</ul>')



html.write('</body></html>')
html.close()

