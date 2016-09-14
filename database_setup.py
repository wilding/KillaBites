# Configuration
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()


class Ingredient(Base):
    __tablename__ = 'ingredient'
    id = Column(Integer, primary_key=True)
    name = Column(String(500), nullable=False)
    picture = Column(String(2000))
    group = Column(String(500), nullable=False)
    january = Column(Boolean)
    february = Column(Boolean)
    march = Column(Boolean)
    april = Column(Boolean)
    may = Column(Boolean)
    june = Column(Boolean)
    july = Column(Boolean)
    august = Column(Boolean)
    september = Column(Boolean)
    october = Column(Boolean)
    november = Column(Boolean)
    december = Column(Boolean)

    # JSON
    @property
    def serialize(self):
        ingredient_dict = {
            'name': self.name,
            'id': self.id,
            'picture': self.picture,
            'group': self.group,
            'january': self.january,
            'february': self.february,
            'march': self.march,
            'april': self.april,
            'may': self.may,
            'june': self.june,
            'july': self.july,
            'august': self.august,
            'september': self.september,
            'october': self.october,
            'november': self.november,
            'december': self.december
        }
        return ingredient_dict


# # Class
# class User (Base):
#    # Table Info
#    __tablename__ = 'user'
#    # Mappers
#    name
#    email
#    picture
#    id
#    recipe_list?
#    favorites_list?
#    course list?
#    type list ?
#    cuisine list?
#    season list?
#    occasion list?
#    # JSON
#
#
# # Class
# class Recipe (Base):
#    # Table Info
#    __tablename__ = 'recipe'
#    # Mappers
#    name
#    id
#    photos
#    ingredients
#    instructions
#    courses
#    types
#    cuisines
#    seasons
#    occasions
#    time
#    calories
#    sources
#    author id
#    vegetarian
#    comments
#    score
#    comments toggle
#    notes
#    # JSON


# Configuration
engine = create_engine('postgresql://vagrant:QB8LLMY)rgr8387e#Wz>Uehn@@localhost/killabites')
Base.metadata.create_all(engine)
