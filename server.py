import psycopg2
import bcrypt
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = 'SECRET KEY'


## HOME PAGE 

@app.route('/')
def index():
    user_id = session.get('user_id')
    user_name = request.cookies.get('user_name')
    return render_template('index.html')








## LOGIN / LOGOUT
# @app.route('/login_page')
# def add_user():
#     user_id = request.cookies.get('user_id')
    
#     return render_template('login.html')


# @app.route('/login_page_action', methods=['POST'])
# def login_page_action():
    
#     return 








app.run(debug=True)