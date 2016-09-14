from flask import Flask, render_template, url_for, request, redirect, flash, jsonify

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload_all
from database_setup import Base, Ingredient

from datetime import datetime

app = Flask(__name__)

# connect to database
engine = create_engine('postgresql://vagrant:QB8LLMY)rgr8387e#Wz>Uehn@@localhost/killabites')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


month_dict = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}


# Homepage
@app.route('/')
def homepage():
    month_num = datetime.now().month
    month = month_dict[month_num]
    if month_num == 1:
        ingredients = session.query(Ingredient).order_by(Ingredient.group).filter_by(january=True).all()
    elif month_num == 2:
        ingredients = session.query(Ingredient).order_by(Ingredient.group).filter_by(february=True).all()
    elif month_num == 3:
        ingredients = session.query(Ingredient).order_by(Ingredient.group).filter_by(march=True).all()
    elif month_num == 4:
        ingredients = session.query(Ingredient).order_by(Ingredient.group).filter_by(april=True).all()
    elif month_num == 5:
        ingredients = session.query(Ingredient).order_by(Ingredient.group).filter_by(may=True).all()
    elif month_num == 6:
        ingredients = session.query(Ingredient).order_by(Ingredient.group).filter_by(june=True).all()
    elif month_num == 7:
        ingredients = session.query(Ingredient).order_by(Ingredient.group).filter_by(july=True).all()
    elif month_num == 8:
        ingredients = session.query(Ingredient).order_by(Ingredient.group).filter_by(august=True).all()
    elif month_num == 9:
        ingredients = session.query(Ingredient).order_by(Ingredient.group).filter_by(september=True).all()
    elif month_num == 10:
        ingredients = session.query(Ingredient).order_by(Ingredient.group).filter_by(october=True).all()
    elif month_num == 11:
        ingredients = session.query(Ingredient).order_by(Ingredient.group).filter_by(november=True).all()
    elif month_num == 12:
        ingredients = session.query(Ingredient).order_by(Ingredient.group).filter_by(december=True).all()
    return render_template('homepage.html', ingredients=ingredients, month=month)


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
