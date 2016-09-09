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

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/ingredient/add/', methods=['GET', 'POST'])
def addIngredient():
    if request.method == 'POST':
        newingredient = Ingredient(
            name=request.form['name'],
            picture=request.form['picture'],
            group=request.form['group'],
            january=request.form['january'],
            february=request.form['february'],
            march=request.form['march'],
            april=request.form['april'],
            may=request.form['may'],
            june=request.form['june'],
            july=request.form['july'],
            august=request.form['august'],
            september=request.form['september'],
            october=request.form['october'],
            november=request.form['november'],
            december=request.form['december'])
        session.add(newingredient)
        session.commit()
        flash('Ingredient added!')
        return redirect(url_for('homepage'))
    else:
        return render_template('newingredient.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
