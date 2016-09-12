from flask import Flask, render_template, url_for, request, redirect, flash, jsonify

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload_all
from database_setup import Base, Ingredient

app = Flask(__name__)

# connect to database
engine = create_engine('sqlite:///killabites.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# Homepage
@app.route('/')
def homepage():
    ingredients = session.query(Ingredient).order_by(Ingredient.group).all()
    return render_template('homepage.html', ingredients=ingredients)


# Add Ingredient
@app.route('/ingredient/add/', methods=['GET', 'POST'])
def addIngredient():
    if request.method == 'POST':
        month_bool = get_month_bool(request.form)
        newingredient = Ingredient(
            name=request.form['name'],
            picture=request.form['picture'],
            group=request.form['group'],
            january=month_bool[0],
            february=month_bool[1],
            march=month_bool[2],
            april=month_bool[3],
            may=month_bool[4],
            june=month_bool[5],
            july=month_bool[6],
            august=month_bool[7],
            september=month_bool[8],
            october=month_bool[9],
            november=month_bool[10],
            december=month_bool[11])
        session.add(newingredient)
        session.commit()
        flash('Ingredient added!')
        return redirect(url_for('homepage'))
    else:
        return render_template('newingredient.html')


# Edit Ingredient
@app.route('/ingredient/edit/<int:ingredient_id>/', methods=['GET', 'POST'])
def editIngredient(ingredient_id):
    ingredient = session.query(Ingredient).filter_by(id=ingredient_id).one()
    if request.method == 'POST':
        if request.form['name']:
            ingredient.name = request.form['name']
        if request.form['picture']:
            ingredient.picture = request.form['picture']
        if request.form['group']:
            ingredient.group = request.form['group']
        month_bool = get_month_bool(request.form)
        ingredient.january = month_bool[0]
        ingredient.february = month_bool[1]
        ingredient.march = month_bool[2]
        ingredient.april = month_bool[3]
        ingredient.may = month_bool[4]
        ingredient.june = month_bool[5]
        ingredient.july = month_bool[6]
        ingredient.august = month_bool[7]
        ingredient.september = month_bool[8]
        ingredient.october = month_bool[9]
        ingredient.november = month_bool[10]
        ingredient.december = month_bool[11]
        session.add(ingredient)
        session.commit()
        flash(ingredient.name + ' edited!')
        return redirect(url_for('homepage'))
    else:
        return render_template('editingredient.html', ingredient=ingredient)


# Delete Ingredient
@app.route('/ingredient/delete/<int:ingredient_id>/', methods=['GET', 'POST'])
def deleteIngredient(ingredient_id):
    ingredient = session.query(Ingredient).filter_by(id=ingredient_id).one()
    if request.method == 'POST':
        session.delete(ingredient)
        session.commit()
        flash('Ingredient deleted!')
        return redirect(url_for('homepage'))
    else:
        return render_template('deleteingredient.html', ingredient=ingredient)


# month_bool helper function
def get_month_bool(form):
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    month_bool = []
    for month in months:
        if form.get(month):
            month_bool.append(True)
        else:
            month_bool.append(False)
    return month_bool


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
