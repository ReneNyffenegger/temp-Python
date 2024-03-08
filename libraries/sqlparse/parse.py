import sqlparse

stmt = '''
  select
     clt.id                          client_id,
     clt.name                        client_name,
     sal.val *  sal.items         as total_price,
    'foo bar baz: ' || sal.txt    as conc
  from
     client clt                                  join
     sale   sal on clt.id = sal.client_id
'''


def printTokenTree(lvl, token):
   if hasattr(token, 'tokens'):
      for t in token.tokens:
          printTokenTree(lvl+1, t)
   else:
      if not token.is_whitespace:
         print( ('  ' *lvl) + token.value)

ast = sqlparse.parse(stmt)[0]

printTokenTree(0, ast)
