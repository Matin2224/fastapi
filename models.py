from sqlalchemy.orm import relationship

from database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Text


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, index=True)
    password = Column(String)
    # phone = Column(String, unique=True)
    # author = relationship("Author", back_populates="user")


# class Author(User):
#     __tablename__ = "authors"
#     id = Column(Integer, primary_key=True)
#
#     user_id = Column(Integer, ForeignKey("users.id"))
#
#     user = relationship("User", back_populates="contact")
#     post = relationship("Post", back_populates="author")
#
# class Post(Base):
#     __tablename__ = "posts"
#     id = Column(Integer, primary_key=True)
#     title = Column(String(50), index=True)
#     description = Column(Text)
#     image_url = Column(String, nullable=True,unique=True)
#     author_id = Column(Integer, ForeignKey("author.id"))
#     author = relationship("Author", back_populates="contacts")
