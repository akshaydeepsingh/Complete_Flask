from config.dbConnection import Base,db_session
from sqlalchemy import Column,Integer,String,ForeignKey,DateTime,func,Table
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

channels = Table("channelpost",
Base.metadata,
Column("postid",Integer,ForeignKey("posts.id")),
Column("channelid",Integer,ForeignKey("channel.id")))

class Channel(Base):
    __tablename__="channel"
    id = Column(Integer,primary_key=True)
    name=  Column(String(100))