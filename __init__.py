from flask import Flask, render_template, url_for, request, redirect, flash, jsonify

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload_all
from database_setup import Base, Ingredient, Recipe

from datetime import datetime, timedelta

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
    # session.rollback()
    current_month = datetime.now().month
    ingredients = session.query(Ingredient).filter(Ingredient.months.any(current_month)).order_by(Ingredient.group, Ingredient.name).all()
    return render_template('homepage.html', ingredients=ingredients, month=month_dict[current_month])


# Full Menu
@app.route('/menu/')
def menupage():
    """docstring for menupage"""
    # session.rollback()
    recipes = session.query(Recipe).all()
    return render_template('menupage.html', recipes=recipes, month_dict=month_dict)


# Full Chart
@app.route('/chart/')
def chartpage():
    """docstring for chartpage"""
    ingredients = session.query(Ingredient).order_by(Ingredient.group, Ingredient.name).all()
    return render_template('chartpage.html', ingredients=ingredients)


# Ingredient CRUD


# Add Ingredient
@app.route('/ingredient/add/', methods=['GET', 'POST'])
def newIngredient():
    """docstring for newIngredient"""
    if request.method == 'POST':
        newingredient = Ingredient(
            name=request.form['name'],
            picture=request.form['picture'],
            group=request.form['group'],
            months=parse_months(request.form),
            alts=request.form.getlist('alt'),
            storage=request.form['storage'])
        session.add(newingredient)
        session.commit()
        flash(newingredient.name + ' added!')
        return redirect(url_for('chartpage'))
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
        ingredient.alts = request.form.getlist('alt')
        ingredient.months = parse_months(request.form)
        session.add(ingredient)
        session.commit()
        flash(ingredient.name + ' edited!')
        return redirect(url_for('chartpage'))
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
        return redirect(url_for('chartpage'))
    else:
        return render_template('deleteingredient.html', ingredient=ingredient)


# Recipe CRUD


# View Recipe
@app.route('/recipe/<int:recipe_id>/')
def viewRecipe(recipe_id):
    """docstring for viewRecipe"""
    recipe = session.query(Recipe).filter_by(id=recipe_id).one()
    return render_template('viewrecipe.html', recipe=recipe, month_dict=month_dict)


# New Recipe
@app.route('/recipe/new/', methods=['GET', 'POST'])
def newRecipe():
    """docsting for newRecipe"""
    if request.method == 'POST':
        newrecipe = Recipe(
            name=request.form['name'],
            pictures=request.form.getlist('pictures'),
            gif=request.form['gif'],
            sources=request.form.getlist('sources'),
            time=parse_time(request.form),
            total_yield=request.form['total_yield'],
            calories=request.form['calories'] if request.form.get('calories') else 0,
            vegetarian=True if request.form.get('vegetarian') else False,
            months=parse_months(request.form),
            cuisines=request.form.getlist('cuisines'),
            groups=request.form.getlist('groups'),
            courses=parse_courses(request.form),
            occasions=request.form.getlist('occasions'),
            ingredients=request.form.getlist('ingredients'),
            instructions=parse_instructions(request.form))
        session.add(newrecipe)
        session.commit()
        flash(newrecipe.name + ' added!')
        return redirect(url_for('menupage'))
    else:
        return render_template('newrecipe.html')


# Edit Recipe
@app.route('/recipe/edit/<int:recipe_id>/', methods=['GET', 'POST'])
def editRecipe(recipe_id):
    """docstring for editRecipe"""
    recipe = session.query(Recipe).filter_by(id=recipe_id).one()
    if request.method == 'POST':
        if request.form['name']:
            recipe.name = request.form['name']
        if request.form['gif']:
            recipe.gif = request.form['gif']
        if request.form['total_yield']:
            recipe.total_yield = request.form['total_yield']
        if request.form['calories']:
            recipe.calories = request.form['calories']
        recipe.pictures = request.form.getlist('pictures')
        recipe.sources = request.form.getlist('sources')
        recipe.time = parse_time(request.form)
        recipe.vegetarian = True if request.form.get('vegetarian') else False
        recipe.months = parse_months(request.form)
        recipe.cuisines = request.form.getlist('cuisines')
        recipe.groups = request.form.getlist('groups')
        recipe.courses = parse_courses(request.form)
        recipe.occasions = request.form.getlist('occasions')
        recipe.ingredients = request.form.getlist('ingredients')
        recipe.instructions = parse_instructions(request.form)
        session.add(recipe)
        session.commit()
        flash(recipe.name + ' edited!')
        return redirect(url_for('menupage'))
    else:
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
        return redirect(url_for('menupage'))
    else:
        return render_template('deleterecipe.html', recipe=recipe)


# Helper Functions


# month parser helper function
def parse_months(form):
    """docstring for parse_months"""
    output = []
    for i in range(1, 13):
        if form.get(month_dict[i][:3]):
            output.append(i)
    return output


# timedelta parser helper function
def parse_time(form):
    days = int(form['days']) if form.get('days') else 0
    hours = int(form['hours']) if form.get('hours') else 0
    minutes = int(form['minutes']) if form.get('minutes') else 0
    seconds = int(form['seconds']) if form.get('seconds') else 0
    return timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)


# course parser helper function
def parse_courses(form):
    """docstring for parse_courses"""
    output = []
    if form.get('breakfast'):
        output.append('Breakfast')
    if form.get('dinner'):
        output.append('Lunch & Dinner')
    if form.get('dessert'):
        output.append('Dessert')
    if form.get('basics'):
        output.append('Basics')
    return output


# instructions parser helper function
def parse_instructions(form):
    """docstring for parse_instructions"""
    text_list = form.getlist('instructions-text')
    photo_list = form.getlist('instructions-photo')
    video_list = form.getlist('instructions-video')
    gif_list = form.getlist('instructions-gif')
    note_list = form.getlist('instructions-note')
    output = []
    for i in range(len(text_list)):
        instruction_dict = {}
        instruction_dict['text'] = text_list[i]
        instruction_dict['photo'] = photo_list[i]
        instruction_dict['video'] = video_list[i]
        instruction_dict['gif'] = gif_list[i]
        instruction_dict['note'] = note_list[i]
        output.append(instruction_dict)
    return output


# set up server to listen to incoming requests
if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
