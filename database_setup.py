# Configuration
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Interval
from sqlalchemy.dialects.postgresql import ARRAY, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()


class Ingredient(Base):
    """docstring for Ingredient class"""
    __tablename__ = 'ingredient'
    id = Column(Integer, primary_key=True)
    name = Column(String(500), nullable=False)
    picture = Column(String(9999))
    group = Column(String(500), nullable=False)
    months = Column(ARRAY(Integer))
    alts = Column(ARRAY(String(500)))
    storage = Column(String(9999))

    @property
    def serialize(self):
        """Instance method, returns a dictionary
        with column names as keywords for the instance's
        associated values. Output can easily be jsonified."""
        ingredient_dict = {
            'name': self.name,
            'id': self.id,
            'picture': self.picture,
            'group': self.group,
            'months': self.months,
            'alts': self.alts,
            'storage': self.storage
        }
        return ingredient_dict


class Recipe(Base):
    """docstring for Recipe class"""
    __tablename__ = 'recipe'
    id = Column(Integer, primary_key=True)
    name = Column(String(500), nullable=False)
    pictures = Column(ARRAY(String(9999)))
    gif = Column(String(9999))
    sources = Column(ARRAY(String(9999)))
    time = Column(Interval)
    total_yield = Column(String(500))
    calories = Column(Integer)
    vegetarian = Column(Boolean)
    months = Column(ARRAY(Integer))
    cuisines = Column(ARRAY(String(500)))
    groups = Column(ARRAY(String(500)))
    courses = Column(ARRAY(String(500)))
    occasions = Column(ARRAY(String(500)))
    ingredients = Column(ARRAY(String(9999)))
    instructions = Column(JSON)

    @property
    def serialize(self):
        """Instance method, returns a dictionary
        with column names as keywords for the instance's
        associated values. Output can easily be jsonified."""
        recipe_dict = {
            'name': self.name,
            'id': self.id,
            'pictures': self.pictures,
            'gif': self.gif,
            'sources': self.sources,
            'time': str(self.time),
            'total_yield': self.total_yield,
            'calories': self.calories,
            'vegetarian': self.vegetarian,
            'months': self.months,
            'cuisines': self.cuisines,
            'groups': self.groups,
            'courses': self.courses,
            'occasions': self.occasions,
            'ingredients': self.ingredients,
            'instructions': self.instructions
        }
        return recipe_dict



class Wine(Base):
    """docstring for Wine class"""
    __tablename__ = 'wine'
    id = Column(Integer, primary_key=True)
    label = Column(String(9999))
    picture = Column(String(9999))
    name = Column(String(9999))
    winery = Column(ARRAY(String(9999)))
    vintage = Column(Integer)
    variety = Column(ARRAY(String(500)))
    region = Column(String(9999))
    rating = Column(Integer)
    notes = Column(ARRAY(String(9999)))
    pairings = Column(ARRAY(String(9999)))
    sparkling = Column(Boolean)
    dessert = Column(Boolean)
    favorite = Column(Boolean)

    @property
    def serialize(self):
        """Instance method, returns a dictionary
        with column names as keywords for the instance's
        associated values. Output can easily be jsonified"""
        wine_dict = {
            'id': self.id,
            'name': self.name,
            'label' : self.label,
            'picture': self.picture,
            'winery': self.winery,
            'vintage': self.vintage,
            'variety': self.variety,
            'region': self.region,
            'rating': self.rating,
            'notes': self.notes,
            'pairings': self.pairings,
            'sparkling': self.sparkling,
            'dessert': self.dessert,
            'favorite':self.favorite
        }
        return wine_dict


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


# Configuration
engine = create_engine('postgresql://vagrant:QB8LLMY)rgr8387e#Wz>Uehn@@localhost/killabites')
Base.metadata.create_all(engine)
