import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False, unique=True)
    password = Column(String)
    email = Column(String(250), nullable = False, unique = True)
    first_name = Column(String(250), nullable = False)
    last_name = Column(String(250))
    posts = relationship('Post')
    comments = relationship('Comment')
    

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable = False)
    comments = relationship('Comment')

    def to_dict(self):
        return {}


class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(500), nullable = False)
    author_id = Column(Integer, ForeignKey('user.id'), nullable = False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable = False)
  

    def to_dict(self):
        return {}


asociation_table = Table('followers', Base.metadata,
Column('user_from_id', Integer, ForeignKey('user.id')),
Column('user_for_id', Integer, ForeignKey('user.id'))
)

   



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')