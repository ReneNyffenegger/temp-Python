import sqlalchemy
import os

engine = sqlalchemy.create_engine(f'sqlite:///{os.getcwd()}/a.db')

print(dir(engine))
