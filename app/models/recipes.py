from .database import Base
from sqlalchemy import Column,String,Integer,Boolean,Text,ForeignKey
from sqlalchemy.orm import relationship
from passlib.hash import pbkdf2_sha256


class User(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True)
    username=Column(String(length=25),nullable=False,unique=True)
    email=Column(String(80),nullable=False)
    passwd_hash=Column(Text)
    recipes=relationship("Recipe",back_populates="user")



    def generate_password(self,password):
        self.passwd_hash=pbkdf2_sha256.hash(password)

    def check_password(self,password):
        return pbkdf2_sha256.verify(password,self.passwd_hash)





class Recipe(Base):
    __tablename__='recipes'
    id=Column(Integer,primary_key=True)
    title=Column(String,nullable=False)
    preparation_time=Column(Integer,nullable=False)
    description=Column(Text,nullable=False)
    user_id=Column(Integer,ForeignKey('users.id'))
    user=relationship('User',back_populates='recipes')

    def __repr__(self):
        return f'<Recipe {self.title}>'



