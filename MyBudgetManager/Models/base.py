from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

f = open("base_converter.txt", "r")

first_line = f.readline()
second_line = f.readline()
foundable_char = '\''

at_home = first_line[first_line.find(foundable_char):].rstrip()
not_at_home = second_line[second_line.find(foundable_char):].rstrip()

try:
    engine = create_engine(at_home)
except:
    engine = create_engine(not_at_home)

session = Session(engine)

Base = declarative_base()
