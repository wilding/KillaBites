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

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
