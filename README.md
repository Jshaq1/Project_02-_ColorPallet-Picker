<div align="center">

  <h1 align="center">Hue - Color Pallet Generator</h1>

  <p align="center">
    A colour pallet generator for web/graphic designers allowing users to automatically generate optimal pallets with complimentary colours and save these for later use.
    <br />
    <a href="https://hue-pallet.herokuapp.com/">View Demo</a>
    <br/>
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#features">Features</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#useful resources">Useful Resources</a></li>
      </ul>
    </li>
  </ol>
</details>
<br/>


## About the project
![Screenshot of project](/Project_02-_ColorPallet-Picker/Screenshot%202023-03-14%20at%2012.59.21%20pm.png?raw=true"HUE")
<br/>
 <p align="center">
Designed as a quickly usable aid in my own personal design process allowing me to quickly generate and save color pallets on the fly as well as source the RGB codes for said color pallets. 

<br/>


# Features (planned/complete)
- User Profile [x]
    - User Auth [x]
    - Cookie use [x]
    - Pallet Save [x]
- Pallet Generator
    - Access API [x]
    - Return hex/rgb codes [x]
    - Copy code on click [x]
    - Save pallet with name [x]
    - Complimentary colour combinations [x]
    - Colour lock [ ]
    - Color wheel [ ]


# Built With 

- Python
- pip
- Flask
- MYSQL
- Heroku 
- Bcrypt
- Jinja2
- Psycopg2
- Gunicorn


# Getting Started
### Prerequisites

 ```sh
 python -m ensurepip --upgrade
 ```
### Installation
 1. Clone the repo
    ```sh
    git clone https://github.com/Jshaq1/Project_02-_ColorPallet-Picker.git
    ```

 2. Install packages
    ```sh
    pip install -r requirements.txt
    ```

### Useful Resources 
- http://colormind.io/

<br/>

# Challenges

## API 
- The API I decided to use prooved to have some difficulties around functionatliy outside of generating random pallets, I initially wanted to include some form of color picker which could source from images but this really never eventuated. 

- The API also seems to sometimes not accept the request, not sure if thats something on my end or the API but I was unable to fix this. 

- Because I am generating the colors inside Python as apposed to via Javascript I felt that it was hard to manipulate them in any meaningful way prior to displaying them. Potentially something to revisit. 


## Javascript 
- Realistically the Javascript in this project is almost none exitent and it mostly because I struggled to get anything that could interact with Python. 

- Would have loved to add functionality to the pallet like locking a particular colour or being able to shift them around into different orders. Just wasnt something I felt like I was capable of without refactoring how my templates were generated. 

- My Login / signup is just not ideal. Its clunky and gives very little user response. 

- Alot of little things missing like confirmation of copy to clipboard, confirmation of login, confirmation of signup, login errors, save errors, saving without a name ect. 


## Python
- I believe that the way my site functions in terms of user experience is flawd, there should be no reason for the page to reload every time someone requests a pallet and same goes for storing the pallet information. If you want to save but are no logged in you need to log in which then basically means you lose the pallet you were looking at initially which is not ideal 


## CSS
- Had a hard time creating flexible ways to display the colour information. Resorted to using purely RGB codes. 

- Navigation was a difficult task as the bar doesnt really suit pages other than the home page as it was designed around the bars of colour. 



