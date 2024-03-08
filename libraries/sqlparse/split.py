import sqlparse

stmts = '''

   select * from dual;
   select 42 + 13;
   insert into dest
   select
      x,
      y
   from
      src

'''

for i, stmt in enumerate(sqlparse.split(stmts)):
    print(str(i) + ': ' + stmt)
