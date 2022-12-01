from config.dbConnection import Base
from sqlalchemy import Column,Text,Integer,Boolean,DateTime,func,String
from sqlalchemy.orm import relationship
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema,fields,schema
from model.posts import Posts,PostsSchema
#define table structure
class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    firstname = Column(Text(30))
    lastname = Column(Text(25),nullable=True)
    email = Column(String(100),nullable=False)
    password = Column(Text(100))
    registerdate = Column(DateTime, server_default=func.now())
    posts = relationship("Posts",backref="user",lazy= "dynamic")
 

    def __init__(self,email,password,firstname,lastname=None):
        self.email = email
        self.password = password
        self.firstname = firstname
        self.lastname = lastname



        
class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        
        
