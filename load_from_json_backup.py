import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Ingredient, Recipe

engine = create_engine('postgresql://vagrant:QB8LLMY)rgr8387e#Wz>Uehn@@localhost/killabites')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


with open('backups/ingredients_2021-01-15', 'r') as json_data:
    full_data = json.load(json_data)
    ingredients = full_data['Ingredients']
    for i in ingredients:
        print('adding ' + i['name'] + ' to database...')
        newingredient = Ingredient(
            name=i['name'],
            picture=i['picture'],
            group=i['group'],
            months=i['months'],
            alts=i['alts'],
            storage=i['storage'])
        session.add(newingredient)
    session.commit()


with open('backups/recipes_2023-05-25.json', 'r') as json_data:
    full_data = json.load(json_data)
    recipes = full_data['Recipes']
    for r in recipes:
        print('adding ' + r['name'] + ' to database...')
        newrecipe = Recipe(
            name=r['name'],
            pictures=r['pictures'],
            sources=r['sources'],
            time=r['time'],
            total_yield=r['total_yield'],
            calories=r['calories'],
            vegetarian=r['vegetarian'],
            months=r['months'],
            cuisines=r['cuisines'],
            groups=r['groups'],
            courses=r['courses'],
            occasions=r['occasions'],
            ingredients=r['ingredients'],
            instructions=r['instructions'],
            gif=r['gif'])
        session.add(newrecipe)
    session.commit()

