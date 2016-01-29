# Configuration
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()




# Class
class User (Base):
	# Table Info
	__tablename__ = 'user'
	# Mappers
	name
	email
	picture
	id
	recipe_list?
	favorites_list?
	course list?
	type list ?
	cuisine list?
	season list?
	occasion list?
	# JSON



# Class
class Recipe (Base):
	# Table Info
	__tablename__ = 'recipe'
	# Mappers
	name
	id
	photos
	ingredients
	instructions
	courses
	types
	cuisines
	seasons
	occasions
	time
	calories
	sources
	author id
	vegetarian
	comments
	score
	comments toggle
	notes
	# JSON


# Configuration
engine = create_engine('sqlite:///killabites.db')
Base.metadata.create_all(engine)