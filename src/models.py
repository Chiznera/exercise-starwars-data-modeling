import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
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
    favorites = relationship("favorites")
    username = Column(String(256), nullable=False)
    first_name = Column(String(256), nullable=False)
    last_name = Column(String(256), nullable=False)
    email = Column(String(256), nullable=False)
    password = Column(String(256), nullable=False)



class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    character_id = Column(Integer, ForeignKey('character.id'))


class Character(Base):
    __tablename__ = 'charcter'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    favorites = relationship("favorites")
    name = Column(String(256))
    birth_year = Column(Integer)
    eye_color = Column(String(256), nullable=False)
    gender = Column(String(256), nullable=False)
    hair_color = Column(String(256), nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    skin_color = Column(String(256), nullable=False)
    homeworld = Column(String(256), nullable=False)
    url = Column(String(256), nullable=False)

class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    favorites = relationship("favorites")
    name = Column(String(256))
    diameter = Column(Integer)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(Integer)
    gravity = Column(Integer, nullable=False)
    population = Column(Integer, nullable=False)
    climate = Column(String(256), nullable=False)
    terrain = Column(String(256), nullable=False)
    surface_water = Column(String(256), nullable=False)
    url = Column(String(256), nullable=False)

    # def to_dict(self):
    #     return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

# ForeignKey('person.id')