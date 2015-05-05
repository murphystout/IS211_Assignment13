from flask import Flask, render_template, request, redirect, session, g, url_for, abort, flash
import os.path
import time
import re


# import sqlite3
# conn = sqlite3.connect('hw13.db')

#configuration
DATABASE = 'hw13.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def before_request():
	g.db = connect_db()
	
@app.teardown_request
def teardown_request(exception):
	db = getattr(g, 'db', None)
	if db is not None:
		db.close()




@app.route('/login', methods = ['POST','GET'])
def login():
	return render_template('login.html')
	
	
if __name__ == '__main__':
    app.run()