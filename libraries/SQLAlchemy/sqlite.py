import sqlalchemy
import os

db_name = 'a.db'

if os.path.exists(db_name):
   print(f'deleting {db_name}')
   os.remove(db_name)

eng = sqlalchemy.create_engine(f'sqlite:///{os.getcwd()}/{db_name}')

with eng.connect() as con:
     con.execute(sqlalchemy.text('create table tab_one (id integer, txt text)'))

     con.execute(
         sqlalchemy.text("insert into tab_one (id, txt) values (:i, :t)"), [
           {'i': 42, 't': 'forty-two'  },
           {'i': 99, 't': 'ninety-nine'}
         ]
     )

     con.commit()
  #  con.rollback()


     res = con.execute(sqlalchemy.text('select * from tab_one'))
     print(res.all())


