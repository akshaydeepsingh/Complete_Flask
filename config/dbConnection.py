from sqlalchemy.ext import declarative
from sqlalchemy.orm import sessionmaker,scoped_session
from sqlalchemy import create_engine



DATABASE_URL = "mysql://asr:1337@127.0.0.1:3306/my_stuff"
engine = create_engine(DATABASE_URL,pool_size = 10)  #db_connection

db_session = scoped_session(sessionmaker(bind=engine)) #db_session managment

Base = declarative.declarative_base()
Base.query = db_session.query_property()
