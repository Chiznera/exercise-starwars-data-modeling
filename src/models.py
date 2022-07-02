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
    username = Column(String(256), nullable=False)
    first_name = Column(String(256), nullable=False)
    last_name = Column(String(256), nullable=False)
    email = Column(String(256), nullable=False)

class Favorite(Base):
    __tablename__ = 'favorite'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(String(256), nullable=False)
    planet_id = Column(String(256), nullable=False)
    character_id = Column(String(256), nullable=False)


class Character(Base):
    __tablename__ = 'charcter'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    birth_year = Column(String(256))
    eye_color = Column(String(256), nullable=False)
    gender = Column(String(256), nullable=False)
    hair_color = Column(String(256), nullable=False)
    height = Column(String(256), nullable=False)
    mass = Column(String(256), nullable=False)
    skin_color = Column(String(256), nullable=False)
    homeworld = Column(String(256), nullable=False)
    url = Column(String(256), nullable=False)

class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    diameter = Column(String(256))
    rotation_period = Column(String(256), nullable=False)
    orbital_period = Column(Integer, ForeignKey('person.id'))
    gravity = Column(String(256), nullable=False)
    population = Column(String(256), nullable=False)
    climate = Column(String(256), nullable=False)
    terrain = Column(String(256), nullable=False)
    surface_water = Column(String(256), nullable=False)
    url = Column(String(256), nullable=False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')