# Configuration
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
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
