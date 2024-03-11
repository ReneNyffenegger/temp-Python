#
#      https://stackoverflow.com/questions/72087411/simple-way-to-parse-sql-subqueries
#
import sqlparse
 
def queries(d):
 
#  print(type(d))
   if type(d) != sqlparse.sql.Token:
      paren = isinstance(d, sqlparse.sql.Parenthesis)
      v = [queries(i) for i in (d if not paren else d[1:-1])]
      subseq, qrs = ''.join(str(i[0]) for i in v), [x for _, y in v for x in y]
      if [*d][paren].value == 'SELECT':
         return '<subquery>', [subseq]+qrs
      return subseq, qrs
   return d, []
 
#
#   Note: the following code does not work anymore if the SELECT keyword follows a new line
#
s="""SELECT
   name,
   email
FROM (
   SELECT *
   FROM
       user
   WHERE
       email IS NOT NULL
)
WHERE
   id IN (SELECT cID FROM customer WHERE points > 5)
"""
 
 
_, subqueries = queries(sqlparse.parse(s)[0])

print('\n\n---------\n\n'.join(subqueries))
print()
 
#for subq in subqueries:
#    print(subq)
