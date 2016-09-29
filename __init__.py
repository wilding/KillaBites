from flask import Flask, render_template, url_for, request, redirect, flash, jsonify

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload_all
from database_setup import Base, Ingredient, Recipe

from datetime import datetime

# initialize flask app
app = Flask(__name__)

# connect to database
engine = create_engine('postgresql://vagrant:QB8LLMY)rgr8387e#Wz>Uehn@@localhost/killabites')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# global month dictionary for quick lookup
month_dict = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}


# Homepage
@app.route('/')
def homepage():
    """docstring for homepage"""
    current_month = datetime.now().month
    ingredients = session.query(Ingredient).filter(Ingredient.months.any(current_month)).order_by(Ingredient.group).all()
    return render_template('homepage.html', ingredients=ingredients, month=month_dict[current_month])


# Full Menu
@app.route('/menu/')
def menupage():
    """docstring for menupage"""
    recipes = session.query(Recipe).all()
    return render_template('menupage.html', recipes=recipes)


# Full Chart
@app.route('/chart/')
def chartpage():
    """docstring for chartpage"""
    ingredients = session.query(Ingredient).order_by(Ingredient.group).all()
    return render_template('chartpage.html', ingredients=ingredients)


# Ingredient CRUD


# Add Ingredient
@app.route('/ingredient/add/', methods=['GET', 'POST'])
def addIngredient():
    """docstring for addIngredient"""
    if request.method == 'POST':
        newingredient = Ingredient(
            name=request.form['name'],
            picture=request.form['picture'],
            group=request.form['group'],
            months=get_months_from_form(request.form),
            storage=request.form['storage'])
        session.add(newingredient)
        session.commit()
        flash(newingredient.name + ' added!')
        return redirect(url_for('homepage'))
    else:
        return render_template('newingredient.html')


# Edit Ingredient
@app.route('/ingredient/edit/<int:ingredient_id>/', methods=['GET', 'POST'])
def editIngredient(ingredient_id):
    """docstring for editIngredient"""
    ingredient = session.query(Ingredient).filter_by(id=ingredient_id).one()
    if request.method == 'POST':
        if request.form['name']:
            ingredient.name = request.form['name']
        if request.form['picture']:
            ingredient.picture = request.form['picture']
        if request.form['group']:
            ingredient.group = request.form['group']
        if request.form['storage']:
            ingredient.storage = request.form['storage']
        ingredient.months = get_months_from_form(request.form)
        session.add(ingredient)
        session.commit()
        flash(ingredient.name + ' edited!')
        return redirect(url_for('homepage'))
    else:
        return render_template('editingredient.html', ingredient=ingredient)


# Delete Ingredient
@app.route('/ingredient/delete/<int:ingredient_id>/', methods=['GET', 'POST'])
def deleteIngredient(ingredient_id):
    """docstring for deleteIngredient"""
    ingredient = session.query(Ingredient).filter_by(id=ingredient_id).one()
    if request.method == 'POST':
        session.delete(ingredient)
        session.commit()
        flash(ingredient.name + ' deleted!')
        return redirect(url_for('homepage'))
    else:
        return render_template('deleteingredient.html', ingredient=ingredient)


# Recipe CRUD


# View Recipe
@app.route('/recipe/<int:recipe_id>/')
def viewRecipe(recipe_id):
    """docstring for viewRecipe"""
    recipe = session.query(Recipe).filter_by(id=recipe_id).one()
    return render_template('viewrecipe.html', recipe=recipe)


# New Recipe
@app.route('/recipe/new/', methods=['GET', 'POST'])
def newRecipe():
    """docsting for newRecipe"""
    # if request.method == 'POST':
        # newrecipe = Recipe(
            # name
            # pictures
            # gif
            # sources
            # time
            # total_yield
            # calories
            # vegetarian
            # months
            # cuisines
            # groups
            # courses
            # occassions
            # ingredients
            # instructions)
        # session.add(newrecipe)
        # session.commit()
        # flash(newrecipe.name + ' added!')
        # return redirect(url_for('homepage'))
    # else:
    return render_template('newrecipe.html')


# Edit Recipe
@app.route('/recipe/edit/<int:recipe_id>/', methods=['GET', 'POST'])
def editRecipe(recipe_id):
    """docstring for editRecipe"""
    recipe = session.query(Recipe).filter_by(id=recipe_id).one()
    # if request.method == 'POST':
        # parse form
        # session.add(recipe)
        # session.commit()
        # flash(recipe.name + ' edited!')
        # return redirect(url_for('viewRecipe', recipe_id=recipe.id))
    # else:
    return render_template('editrecipe.html', recipe=recipe)


# Delete Recipe
@app.route('/recipe/delete/<int:recipe_id>/', methods=['GET', 'POST'])
def deleteRecipe(recipe_id):
    """docstring for deleteRecipe"""
    recipe = session.query(Recipe).filter_by(id=recipe_id).one()
    if request.method == 'POST':
        session.delete(recipe)
        session.commit()
        flash(recipe.name + ' deleted!')
        return redirect(url_for('homepage'))
    else:
        return render_template('deleterecipe.html', recipe=recipe)


# Helper Functions


# month_bool helper function
def get_months_from_form(form):
    """docstring for get_months_from_form"""
    output = []
    for i in range(1, 13):
        if form.get(month_dict[i][:3]):
            output.append(i)
    return output


# set up server to listen to incoming requests
if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
