# Configuration
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
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
    begin_month = Column(Integer, nullable=False)
    end_month = Column(Integer, nullable=False)

    # JSON
    @property
    def serialize(self):
        ingredient_dict = {
            'name': self.name,
            'id': self.id,
            'picture': self.picture,
            'group': self.group,
            'begin_month': self.begin_month,
            'end_month': self.end_month
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
engine = create_engine('sqlite:///killabites.db')
Base.metadata.create_all(engine)
