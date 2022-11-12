
import bcrypt
import requests
from flask import Flask, render_template, request, redirect, session
from database import insert_data, sql_select1, sql_select, delete_pallet
import os

app = Flask(__name__)

secret_key = os.environ.get('secret_key')
print(secret_key)
app.secret_key = secret_key



## HOME PAGE 
@app.route('/', methods=['POST', 'GET'])
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
    colors = results['result']
    
    generated_colors = []
    i = 0
    for row in colors:
        r, g, b = row
        i += 1
        generated_colors.append([r,g,b,i])
        


  
    return render_template('index.html', generated_colors = generated_colors, user_name = user_name, colors=colors)
    
@app.route('/save', methods=['POST', 'GET'])
def save_action():
    user_id = session.get('user_id')
    user_name = request.cookies.get('user_name')
    pallet_name = request.form.get('pallet_name')
    color1 = request.form.get('color_codes1')
    color2 = request.form.get('color_codes2')
    color3 = request.form.get('color_codes3')
    color4 = request.form.get('color_codes4')
    color5 = request.form.get('color_codes5')

    insert_data(f'INSERT INTO saved_pallets (name, color1, color2, color3, color4, color5, user_id) VALUES ( %s , %s , %s , %s , %s , %s , %s )', [pallet_name, color1, color2, color3, color4, color5, user_id])
    
    return redirect('/')



## LOGIN / LOGOUT
@app.route('/login_page')
def log_in():
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


@app.route('/logout')
def log_out_action():

    response = redirect('/')
    
    response.delete_cookie('session')
    
    return response 


## LOAD SAVED / DELETE SAVED
@app.route('/profile')
def profile():
    user_id = session.get('user_id')
    user_name = request.cookies.get('user_name')
    

    results = sql_select('SELECT name, color1, color2, color3, color4, color5 FROM saved_pallets WHERE user_id = %s', [user_id])
    saved_pallets=[]
    for row in results:
        name, color1, color2, color3, color4, color5 = row
        saved_pallets.append([name, color1, color2, color3, color4, color5])
    


    return render_template('profile.html', saved_pallets = saved_pallets, user_name=user_name)

@app.route('/delete_pallet_action', methods=['POST'])
def delete_pallet_action():
    name = request.form.get('name')
    user_id = session.get('user_id')
    delete_pallet(name, user_id)
    print(user_id)
    return redirect('/profile')

if __name__ == '__main__':
    
    app.run(debug=True)



