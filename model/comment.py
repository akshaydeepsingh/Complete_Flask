from config.dbConnection import Base
from sqlalchemy import Column,Integer,String

class Comment(Base):
    __tablename__ = "comments"
    post_id = Column("postid",Integer)
    