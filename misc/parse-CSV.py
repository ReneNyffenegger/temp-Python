import re

nofFields = 3
reText = ';'.join(['([^;]*)'] * nofFields)
print(reText)

csvRe = re.compile( reText )
if m := csvRe.match('foo;bar;baz'):
   print(m[1])
   print(m[2])
   print(m[3])

#while dataLine := data.readline():
#     dataLine = dataLine.rstrip('\n')

#if fields := csvRe.match(dataLine):
#   print(fields[1])
