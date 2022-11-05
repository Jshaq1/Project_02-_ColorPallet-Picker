import psycopg2
import bcrypt
import requests
from flask import Flask, render_template, request, redirect, session
from color import generate_colors
from controller import insert_data, sql_select1

app = Flask(__name__)

app.secret_key = 'SECRET KEY'


## HOME PAGE 

@app.route('/')
def index():
    user_id = session.get('user_id')
    user_name = request.cookies.get('user_name')
    
    url = "http://colormind.io/api/"
    data = {
        "model" : "default",
        "input" : ["N","N","N","N","N"]
    }
    response = requests.post(url, json=data)
    results  = response.json()

    color_one = generate_colors(results['result'][0])
    color_two = generate_colors(results['result'][1])
    color_three = generate_colors(results['result'][2])
    color_four = generate_colors(results['result'][3])
    color_five = generate_colors(results['result'][4])


    return render_template('index.html', 
    color_one = color_one, 
    color_two = color_two, 
    color_three = color_three, 
    color_four = color_four,
    color_five = color_five)
    



## LOGIN / LOGOUT
@app.route('/login_page')
def add_user():
    user_id = request.cookies.get('user_id')
    
    return render_template('login.html')


@app.route('/login_page_action', methods=['POST'])
def login_page_action():
    user_email = request.form.get('email')
    user_password = request.form.get('password')


    results = sql_select1(f'SELECT * FROM users WHERE email = %s', [user_email])
    id, name, email, password_hash =  list(results)
    
    valid = bcrypt.checkpw(user_password.encode(), password_hash.encode())

    if valid:
        id, name, email, password_hash =  list(results)
        response = redirect('/')
        session['user_id'] = f'{id}'
        response.set_cookie('user_name', f'{name}')
    else:
        error = 'You arent registered'
        return redirect('/login_page')
        
    return response


@app.route('/sign_up_action', methods=['POST'])
def sign_up_action():
    user_name = request.form.get('name')
    user_email = request.form.get('email')
    user_password = request.form.get('password')
    encrypt_password = bcrypt.hashpw(user_password.encode(), bcrypt.gensalt()).decode()

    insert_data(f'INSERT INTO users (name, email, password_hash) VALUES (%s, %s, %s)', [user_name, user_email,encrypt_password])
    return redirect('/login_page')



app.run(debug=True)



