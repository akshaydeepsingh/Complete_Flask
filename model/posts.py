from config.dbConnection import Base
from sqlalchemy import Column,Text,Integer,Boolean,DateTime,func,TIMESTAMP,ForeignKey
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy.orm import relationship
from model.comment import Comments
from model.channel import Channel,channels

class Posts(Base):
    __tablename__ = "posts"
    id = Column(Integer,primary_key = True)
    title = Column(Text(150))
    category = Column(Text(50))
    Description = Column(Text(500),nullable = True)
    created_time = Column( TIMESTAMP(timezone=False), nullable=False, server_default=func.now())
    userid = Column(Integer,ForeignKey("user.id"))
    comment = relationship("Comments",backref = 'posts',lazy = "dynamic")
    channel = relationship("Channel",secondary=channels,backref = "posts",lazy= "dynamic")


    def __init__(self,title,category,Description):
        self.title = title
        self.category = category
        self.Description = Description



class PostsSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Posts
        load_instance = True
       

