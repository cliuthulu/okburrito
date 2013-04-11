#database .2 beta
#ok.db

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String #DECIMAl!!!
#sqlalchemy session is a handle to interact with db
from sqlalchemy.orm import sessionmaker
# from sqlalchemy.dialects.postgresql.psycopg2 import psycopg2
# from psycopg2 import psycopg2

# engine = create_engine("sqlite:///ratings.db", echo=False)
# session = scoped_session(sessionmaker(bind=engine, autocommit = False, autoflush = False))

ENGINE = None
Session = None

# OMFG remember to type in column names to the python to sql magic 
# ie) u = models.User(nickname='john', email='john@email.com')
Base = declarative_base()

class User(Base):
	__tablename__ = 'users'

	id = Column(Integer, primary_key=True) 
	screenname = Column(String(64), nullable=False)
	email = Column(String(64), nullable=False)
	password = Column(String(64), nullable=False)
	diet = Column(String(64), nullable=True)
	location = Column(String(64), nullable=True)

class Burrito(Base):
	__tablename__='burritos'

	id = Column(Integer, primary_key=True) 
	diet = Column(String(64), nullable=True)
	resturant = Column(String(64), nullable=True)
	self_sum = Column(String(256), nullable=True)
	monies = Column(String(64), nullable=False) #or do i want this to be a number
	spicy = Column(Integer)
	structure = Column(Integer)
	exotic = Column(Integer)
	size = Column(Integer)
	meat = Column(String(64), nullable=True)

class Question(Base):	
	__tablename__='questions'

	id = Column(Integer, primary_key=True)
	q_id = Column(Integer)
	score = Column(Integer)#Decimal(5,2)
	weight = Column(Integer)#Decimal(2,2)
	user_id = Column(Integer)
	burrito_id = Column(Integer)

def connect():
	global ENGINE
	global Session

	ENGINE = create_engine('sqlite:///ok.db', echo = True)	
	#Session is a class generated by sqlalchemy, using sessionmaker
	Session = sessionmaker(bind=ENGINE)

	return Session()


def main():
    """In case we need this for something"""
    pass

if __name__ == "__main__":
    main()