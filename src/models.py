import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(128)) 
    favorites_id = Column(Integer, ForeignKey('favorites.id'))


class Favorites(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    characters_id = Column(Integer, ForeignKey('character.id'))
    planets_id = Column(Integer, ForeignKey('planet.id'))


class Characters(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))   
    birth_year = Column(String(128)) 
    eye_color = Column(String(128)) 
    gender = Column(String(128)) 
    hair_color = Column(String(128)) 
    height = Column(Integer()) 
    mass = Column(Integer())
    skin_color = Column(String(128))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    films = Column(String(128))
    species = Column(String(128))
    starships = Column(String(128))
    vehicles = Column(String(128))
    url = Column(String(128))
    created = Column(String(128))
    edited = Column(String(128))

class Planets(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(128)) 
    diameter = Column(Integer()) 
    rotation_period = Column(Integer()) 
    orbital_period = Column(Integer()) 
    gravity = Column(Integer()) 
    population = Column(Integer()) 
    climate = Column(String(128)) 
    terrain = Column(String(128)) 
    surface_water = Column(Integer()) 
    residents = Column(String(128)) 
    films = Column(String(128)) 
    url = Column(String(128)) 
    created = Column(String(128)) 
    edited = Column(String(128)) 

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
