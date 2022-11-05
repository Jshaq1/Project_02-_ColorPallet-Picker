import psycopg2
import bcrypt
import requests
from flask import Flask, render_template, request, redirect, session
# from color import pallet_generator

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
    color1 = results['result'][0]
    r, g, b = color1
    color_one =( f'rgb({r},{g},{b})')

    color2 = results['result'][1]
    r2, g2, b2 = color2
    color_two =( f'rgb({r2},{g2},{b2})')

    color3 = results['result'][2]
    r3, g3, b3 = color3
    color_three =( f'rgb({r3},{g3},{b3})')

    color4 = results['result'][3]
    r4, g4, b4 = color4
    color_four =( f'rgb({r4},{g4},{b4})')

    color5 = results['result'][4]
    r5, g5, b5 = color5
    color_five =( f'rgb({r5},{g5},{b5})')

    
    
    return render_template('index.html', color_one = color_one, color_two = color_two, color_three = color_three, color_four = color_four,color_five = color_five)




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
    return 



app.run(debug=True)



