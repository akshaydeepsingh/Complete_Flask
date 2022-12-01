from config.dbConnection import Base
from sqlalchemy import Column,Integer,String,ForeignKey,DateTime,func
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
class Comments(Base):
    __tablename__ = "comments"
    id = Column(Integer,primary_key=True)
    post_id = Column(Integer,ForeignKey("posts.id"))
    user = Column(String(150),nullable=False)
    comment= Column(String(1000))
    timestamp =  Column(DateTime, server_default=func.now())

    def __init__(self,comment,user):
        self.comment = comment
        self.user = user


        

class CommentSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Comments
        load_instance = True


    