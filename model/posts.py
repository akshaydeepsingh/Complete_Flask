from config.dbConnection import Base
from sqlalchemy import Column,Text,Integer,Boolean,DateTime,func,TIMESTAMP
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class Posts(Base):
    __tablename__ = "posts"
    id = Column(Integer,primary_key = True)
    title = Column(Text(150))
    category = Column(Text(50))
    Description = Column(Text(500),nullable = True)
    created_time = Column( TIMESTAMP(timezone=False), nullable=False, server_default=func.now())


    def __init__(self,id,title,category,Description):
        self.id = id
        self.title = title
        self.category = category
        self.Description = Description



class PostsSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Posts
        load_instance = True

