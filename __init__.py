from flask import Flask, render_template, url_for, request, redirect, flash, jsonify

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload_all
from database_setup import Base, Ingredient, Recipe, Wine

from datetime import datetime, timedelta

import os
from werkzeug.utils import secure_filename


# initialize flask app
app = Flask(__name__)

# connect to database
engine = create_engine('postgresql://vagrant:QB8LLMY)rgr8387e#Wz>Uehn@@localhost/killabites')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# global month dictionary for quick lookup
month_dict = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
cuisines = {
    'Asian':
        ['Burmese', 'Chinese', 'Filipino', 'Japanese', 'Korean', 'Thai', 'Vietnamese'],
    'Middle Eastern':
        ['Arab', 'Indian', 'Israeli', 'Lebanese', 'Middle Eastern', 'Persian', 'Turkish'],
    'European':
        ['Eastern European', 'English', 'French', 'German', 'Greek', 'Irish',  'Italian', 'Mediterranean', 'Nordic', 'Portuguese', 'Spanish'],
    'Latin American':
        ['Brazilian', 'Caribbean', 'Central American', 'Mexican', 'South American'],
    'American':
        ['American', 'Cajun', 'Canadian', 'Hawaiian', 'Pacific', 'Southern'],
    'African':
        ['African', 'Ethiopian'],
    'Oceanic':
        ['Indonesian', 'Oceanic', 'Polynesian']
}
regions = ['American', 'European', 'Latin American', 'Asian', 'Middle Eastern', 'Oceanic', 'African']
groups = {
    'Breakfast':
        ['Eggs', 'Meat', 'Vegetable', 'Fruit', 'Oatmeal', 'Toast', 'Pancakes', 'Pastry'],
    'Lunch & Dinner':
        ['Salad', 'Soup', 'Bread', 'Tortilla', 'Rice', 'Pasta', 'Noodles', 'Vegetable', 'Sea', 'Air', 'Land'],
    'Dessert':
        ['Fruit & Cheese', 'Pudding', 'Ice Cream', 'Cheesecake', 'Pastry', 'Cookie', 'Candy', 'Donut', 'Cake'],
    'Basics':
        ['Dairy', 'Stock', 'Sauce', 'Pickle'],
    'Drinks':
        ['Coffee', 'Smoothie', 'Milkshake', 'Beer', 'Wine', 'Tequila', 'Mezcal', 'Gin', 'Whiskey', 'Rum', 'Vodka', 'Brandy']
}
ingredient_groups = ['fruit', 'vegetables', 'herbs', 'nuts', 'sea', 'air', 'land']
ingredient_group_colors = {'fruit': ['#7B1FA2', 'rgba(123, 31, 162, 0.3)'], 'vegetables': ['#43A047', 'rgba(67, 160, 71, 0.3)'], 'herbs': ['#7CB342', 'rgba(124, 179, 66, 0.3)'], 'nuts': ['#6D4C41', 'rgba(109, 76, 65, 0.3)'], 'sea': ['#1E88E5', 'rgba(30, 136, 229, 0.3)'], 'air': ['#FDD835', 'rgba(253, 216, 53, 0.3)'], 'land': ['#E53935', 'rgba(229, 57, 53, 0.3)']}

###############################################################################################################################################################################
    # View Pages
###############################################################################################################################################################################


# Homepage
@app.route('/')
def homepage():
    """docstring for homepage"""
    # session.rollback()
    current_month = datetime.now().month
    fruit = session.query(Ingredient).filter_by(group="fruit").filter(Ingredient.months.any(current_month)).order_by(Ingredient.name).all()
    vegetables = session.query(Ingredient).filter_by(group="vegetables").filter(Ingredient.months.any(current_month)).order_by(Ingredient.name).all()
    herbs = session.query(Ingredient).filter_by(group="herbs").filter(Ingredient.months.any(current_month)).order_by(Ingredient.name).all()
    nuts = session.query(Ingredient).filter_by(group="nuts").filter(Ingredient.months.any(current_month)).order_by(Ingredient.name).all()
    sea = session.query(Ingredient).filter_by(group="sea").filter(Ingredient.months.any(current_month)).order_by(Ingredient.name).all()
    air = session.query(Ingredient).filter_by(group="air").filter(Ingredient.months.any(current_month)).order_by(Ingredient.name).all()
    land = session.query(Ingredient).filter_by(group="land").filter(Ingredient.months.any(current_month)).order_by(Ingredient.name).all()
    ingredients = [fruit, vegetables, herbs, nuts, sea, air, land]
    recipes = session.query(Recipe).filter(Recipe.months.any(current_month)).order_by(Recipe.groups)
    return render_template('viewhomepage.html', ingredients=ingredients, month_dict=month_dict, month=month_dict[current_month], recipes=recipes, Recipe=Recipe, groups=groups)


# Full Chart
@app.route('/chart/')
def chartpage():
    """docstring for chartpage"""
    alpha_fruit = session.query(Ingredient).filter_by(group='fruit').order_by(Ingredient.name).all()
    alpha_vegetables = session.query(Ingredient).filter_by(group='vegetables').order_by(Ingredient.name).all()
    alpha_herbs = session.query(Ingredient).filter_by(group='herbs').order_by(Ingredient.name).all()
    alpha_nuts = session.query(Ingredient).filter_by(group='nuts').order_by(Ingredient.name).all()
    alpha_sea = session.query(Ingredient).filter_by(group='sea').order_by(Ingredient.name).all()
    alpha_air = session.query(Ingredient).filter_by(group='air').order_by(Ingredient.name).all()
    alpha_land = session.query(Ingredient).filter_by(group='land').order_by(Ingredient.name).all()
    month_fruit = session.query(Ingredient).filter_by(group='fruit').order_by(Ingredient.months).all()
    month_vegetables = session.query(Ingredient).filter_by(group='vegetables').order_by(Ingredient.months).all()
    month_herbs = session.query(Ingredient).filter_by(group='herbs').order_by(Ingredient.months).all()
    month_nuts = session.query(Ingredient).filter_by(group='nuts').order_by(Ingredient.months).all()
    month_sea = session.query(Ingredient).filter_by(group='sea').order_by(Ingredient.months).all()
    month_air = session.query(Ingredient).filter_by(group='air').order_by(Ingredient.months).all()
    month_land = session.query(Ingredient).filter_by(group='land').order_by(Ingredient.months).all()
    ingredients = [
        (alpha_fruit, month_fruit),
        (alpha_vegetables, month_vegetables),
        (alpha_herbs, month_herbs),
        (alpha_nuts, month_nuts),
        (alpha_sea, month_sea),
        (alpha_air, month_air),
        (alpha_land, month_land)]
    current_month = datetime.now().month
    return render_template('viewchart.html', ingredients=ingredients, current_month=current_month, month_dict=month_dict, ingredient_groups=ingredient_groups, ingredient_group_colors=ingredient_group_colors)


# Full Menu
@app.route('/menu/')
def menupage():
    """docstring for menupage"""
    # session.rollback()
    recipes = session.query(Recipe).order_by(Recipe.name).all()
    return render_template('viewmenu.html', recipes=recipes, month_dict=month_dict, cuisines=cuisines, groups=groups, regions=regions)

# Wine
@app.route('/wine/')
def winepage():
    """docstring for winepage"""
    wine = session.query(Wine).order_by(Wine.id).all()
    regions = []
    wineries = []
    varieties = []
    timestamp = datetime.now()
    current_year = timestamp.year
    oldest_vintage = current_year
    for w in wine:
        if w.vintage and w.vintage < oldest_vintage:
            oldest_vintage = w.vintage
        parts = w.region.split("-")
        part_builder = ''
        for part in parts:
            if part_builder:
                part_builder += '-'
            part_builder += part
            if part_builder not in regions:
                regions.append(part_builder)
        for wnry in w.winery:
            if wnry not in wineries:
                wineries.append(wnry)
        for vrty in w.variety:
            vrty = vrty.split(" [")[0]
            if vrty not in varieties:
                varieties.append(vrty)
    regions.sort()
    rgns = build_nested_structure(regions)
    wineries.sort()
    varieties.sort()
    year_list = list(range(oldest_vintage, current_year))
    return render_template('viewwine.html', wine=wine, regions=regions, rgns=rgns, wineries=wineries, varieties=varieties, years=year_list)

# Wine
@app.route('/wine/shelf/')
def wineshelf():
    """docstring for wineshelf"""
    wine = session.query(Wine).order_by(Wine.id).all()
    regions = []
    wineries = []
    varieties = []
    timestamp = datetime.now()
    current_year = timestamp.year
    oldest_vintage = current_year
    for w in wine:
        if w.vintage and w.vintage < oldest_vintage:
            oldest_vintage = w.vintage
        parts = w.region.split("-")
        part_builder = ''
        for part in parts:
            if part_builder:
                part_builder += '-'
            part_builder += part
            if part_builder not in regions:
                regions.append(part_builder)
        for wnry in w.winery:
            if wnry not in wineries:
                wineries.append(wnry)
        for vrty in w.variety:
            vrty = vrty.split(" [")[0]
            if vrty not in varieties:
                varieties.append(vrty)
    regions.sort()
    rgns = build_nested_structure(regions)
    wineries.sort()
    varieties.sort()
    year_list = list(range(oldest_vintage, current_year))
    return render_template('viewwineshelf.html', wine=wine, regions=regions, rgns=rgns, wineries=wineries, varieties=varieties, years=year_list)

# View Recipe
@app.route('/recipe/<int:recipe_id>/')
def viewRecipe(recipe_id):
    """docstring for viewRecipe"""
    recipe = session.query(Recipe).filter_by(id=recipe_id).one()
    return render_template('viewrecipe.html', recipe=recipe, month_dict=month_dict)


###############################################################################################################################################################################
    # Ingredient CRUD
###############################################################################################################################################################################


# New Ingredient
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
        return render_template('newingredient.html', month_dict=month_dict, ingredient_groups=ingredient_groups)


# Edit Ingredient
@app.route('/ingredient/edit/<int:ingredient_id>/', methods=['GET', 'POST'])
def editIngredient(ingredient_id):
    """docstring for editIngredient"""
    ingredient = session.query(Ingredient).filter_by(id=ingredient_id).one()
    if request.method == 'POST':
        if request.form['name']:
            ingredient.name = request.form['name']
        if request.form['group']:
            ingredient.group = request.form['group']
        ingredient.picture = request.form['picture']
        ingredient.storage = request.form['storage']
        ingredient.alts = request.form.getlist('alt')
        ingredient.months = parse_months(request.form)
        session.add(ingredient)
        session.commit()
        flash(ingredient.name + ' edited!')
        return redirect(url_for('chartpage'))
    else:
        return render_template('editingredient.html', ingredient=ingredient, month_dict=month_dict, ingredient_groups=ingredient_groups)


# Delete Ingredient
@app.route('/ingredient/delete/<int:ingredient_id>/', methods=['POST'])
def deleteIngredient(ingredient_id):
    """docstring for deleteIngredient"""
    ingredient = session.query(Ingredient).filter_by(id=ingredient_id).one()
    if request.method == 'POST':
        session.delete(ingredient)
        session.commit()
        flash(ingredient.name + ' deleted!')
        return redirect(url_for('chartpage'))


###############################################################################################################################################################################
    # Recipe CRUD
###############################################################################################################################################################################


# New Recipe
@app.route('/recipe/new/', methods=['GET', 'POST'])
def newRecipe():
    """docsting for newRecipe"""
    if request.method == 'POST':
        newrecipe = Recipe(
            name=request.form['title'],
            pictures=request.form.getlist('pictures'),
            sources=request.form.getlist('sources'),
            time=parse_time(request.form),
            total_yield=request.form['total_yield'],
            calories=request.form['calories'] if request.form.get('calories') else 0,
            vegetarian=True if request.form.get('vegetarian') else False,
            months=parse_months(request.form),
            cuisines=request.form.getlist('cuisines'),
            groups=request.form.getlist('groups'),
            courses=request.form.getlist('courses'),
            occasions=request.form.getlist('occasions'),
            ingredients=request.form.getlist('ingredients'),
            instructions=parse_instructions(request.form))
        session.add(newrecipe)
        session.commit()
        flash(newrecipe.name + ' added!')
        return redirect(url_for('viewRecipe', recipe_id=newrecipe.id))
    else:
        return render_template('newrecipe.html', month_dict=month_dict, cuisines=cuisines, groups=groups, regions=regions)


# Edit Recipe
@app.route('/recipe/edit/<int:recipe_id>/', methods=['GET', 'POST'])
def editRecipe(recipe_id):
    """docstring for editRecipe"""
    recipe = session.query(Recipe).filter_by(id=recipe_id).one()
    if request.method == 'POST':
        if request.form['title']:
            recipe.name = request.form['title']
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
        recipe.courses = request.form.getlist('courses')
        recipe.occasions = request.form.getlist('occasions')
        recipe.ingredients = request.form.getlist('ingredients')
        recipe.instructions = parse_instructions(request.form)
        session.add(recipe)
        session.commit()
        flash(recipe.name + ' edited!')
        return redirect(url_for('viewRecipe', recipe_id=recipe.id))
    else:
        return render_template('editrecipe.html', recipe=recipe, month_dict=month_dict, cuisines=cuisines, groups=groups, regions=regions)


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


###############################################################################################################################################################################
    # Wine CRUD
###############################################################################################################################################################################


# New Wine
@app.route('/wine/new/', methods=['GET', 'POST'])
def newWine():
    """docsting for newWine"""
    if request.method == 'POST':
        newwine = Wine(
            name=request.form['name'],
            winery=request.form.getlist('winery'),
            vintage=request.form['vintage'] if request.form.get('vintage') else 0,
            variety=request.form.getlist('variety'),
            region=request.form['region'],
            rating=request.form['rating'] if request.form.get('rating') else 0,
            notes=request.form.getlist('notes'),
            pairings=request.form.getlist('pairings'),
            sparkling=True if request.form.get('sparkling') else False,
            dessert=True if request.form.get('dessert') else False,
            favorite=True if request.form.get('favorite') else False)
        label_file = request.files.get('label')
        picture_file = request.files.get('picture')
        newwine.label = save_uploaded_file(label_file, str(newwine.id) + '-label', 'wine-pics')
        newwine.picture = save_uploaded_file(picture_file, str(newwine.id) + '-bottle', 'wine-pics')
        session.add(newwine)
        session.commit()
        flash(newwine.name + ' added!')
        return redirect(url_for('winepage'))
    else:
        return render_template('newwine.html')


# Edit Wine
@app.route('/wine/edit/<int:wine_id>/', methods=['GET', 'POST'])
def editWine(wine_id):
    """docstring for editWine"""
    wine = session.query(Wine).filter_by(id=wine_id).one()
    if request.method == 'POST':
        if request.form['name']:
            wine.name = request.form['name']
        if request.form['region']:
            wine.region = request.form['region']
        if request.form['vintage']:
            wine.vintage = request.form['vintage']
        if request.form['rating']:
            wine.rating = request.form['rating']
        wine.winery = request.form.getlist('winery')
        wine.variety = request.form.getlist('variety')
        wine.notes = request.form.getlist('notes')
        wine.pairings = request.form.getlist('pairings')
        wine.sparkling = True if request.form.get('sparkling') else False
        wine.dessert = True if request.form.get('dessert') else False
        wine.favorite = True if request.form.get('favorite') else False
        label_file = request.files.get('label')
        picture_file = request.files.get('picture')
        if label_file:
            wine.label = save_uploaded_file(label_file, str(wine.id) + '-label', 'wine-pics')
        if picture_file:
            wine.picture = save_uploaded_file(picture_file, str(wine.id) + '-bottle', 'wine-pics')
        session.add(wine)
        session.commit()
        flash(wine.name + ' edited!')
        return redirect(url_for('winepage'))
    else:
        return render_template('editwine.html', wine=wine)


# Delete Wine
@app.route('/wine/delete/<int:wine_id>/', methods=['GET', 'POST'])
def deleteWine(wine_id):
    """docstring for deleteWine"""
    wine = session.query(Wine).filter_by(id=wine_id).one()
    if request.method == 'POST':
        session.delete(wine)
        session.commit()
        flash(wine.name + ' deleted!')
        return redirect(url_for('winepage'))


###############################################################################################################################################################################
    # JSON
###############################################################################################################################################################################


# Ingredients JSON
@app.route('/ingredient/json/')
@app.route('/chart/json/')
def ingredientsJSON():
    ingredients = session.query(Ingredient).order_by(Ingredient.group, Ingredient.name).all()
    return jsonify(Ingredients=[ingredient.serialize for ingredient in ingredients])


# Recipes JSON
@app.route('/recipe/json/')
@app.route('/menu/json/')
def recipesJSON():
    recipes = session.query(Recipe).order_by(Recipe.courses, Recipe.groups, Recipe.name).all()
    return jsonify(Recipes=[recipe.serialize for recipe in recipes])


# Individual Recipe JSON
@app.route('/recipe/<int:recipe_id>/json/')
def recipeJSON(recipe_id):
    recipe = session.query(Recipe).filter_by(id=recipe_id).one()
    return jsonify(recipe.serialize)

# Wine JSON
@app.route('/wine/json/')
def wineJSON():
    wine = session.query(Wine).all()
    return jsonify(Wine=[w.serialize for w in wine])


###############################################################################################################################################################################
    # Helper Functions
###############################################################################################################################################################################


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


# turn list into nested dict
def build_nested_structure(rawlist):
    tree = {}
    paths = []
    for i in rawlist:
        paths.append(i.split("-"))
    for path in paths:
        current = tree
        for part in path:
            current = current.setdefault(part, {})
    return tree

# Save file
def save_uploaded_file(file_obj, new_filename, upload_folder):
    if file_obj and file_obj.filename != '':
        filename = secure_filename(file_obj.filename)
        ext = os.path.splitext(filename)[1]
        unique_filename = f"{new_filename}{ext}"
        upload_path = os.path.join(app.root_path, 'static', upload_folder)
        file_path = os.path.join(upload_path, unique_filename)
        file_obj.save(file_path)
        return f'/static/{upload_folder}/{unique_filename}'  # or return just unique_filename if you want
    else:
        return ''

###############################################################################################################################################################################
    # Initialize server 
###############################################################################################################################################################################

# set up server to listen to incoming requests
if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
