# Project_02-_ColorPallet-Picker
Project_02 _ColorPallet Picker

https://cryptic-lowlands-04033.herokuapp.com/



## Work Plan
- User Story    [x]
- User Flow     [x]     
- Page Elements [x]
- Wireframes    [x]
- Basic HTML    [x]
- Working API   [x]
- Pyth Server   [x]
- CSS           [x]
- JS            []


## PAGES 
- Home []
    - Color Pallet Generator [x] 
    - Jinja template [x]
    - Css [x]

- Login/signup
    - Signup [x]
    - Password Hash [x] 
    - Login Auth [x]
    - Error message [x] 


# ElEMENTS
## INDEX/HOME
- Nav bar 
    - Logo
    - Login Logout
    - Link to profile

- Image slider                  []
    - Images from DB
    - Rotating
    - Select button

- Colour wheel                  []

- Generated colour pallet
    - Lock button               []
    - Save to profile button    [x]
    - RGB CODES                 [x]

- User saved pallets            [x]
    - Save to user profile      []
    - Generate pallet from      []
      individual colour         []
    - Users profile who made it []


## USER PROFILE
- Nav bar 
    - Logo
    - Logout
    - Home (logo)
    

- User saved pallets
    - Pallets saved previously 
    - Potentially the image they are based on
    - Button to apply pallet to current page
    - Button to copy hex code for colour individually 
    - Suggested pallets




# Struggles

# API 
- The API I decided to use prooved to have some difficulties around functionatliy outside of generating random pallets, I initially wanted to include some form of color picker which could source from images but this really never eventuated. 

- The API also seems to sometimes not accept the request, not sure if thats something on my end or the API but I was unable to fix this. 

- Because I am generating the colors inside Python as apposed to via Javascript I felt that it was hard to manipulate them in any meaningful way prior to displaying them. Potentially something to revisit. 


# Javascript 
- Realistically the Javascript in this project is almost none exitent and it mostly because I struggled to get anything that could interact with Python. 

- Would have loved to add functionality to the pallet like locking a particular colour or being able to shift them around into different orders. Just wasnt something I felt like I was capable of without refactoring how my templates were generated. 

- My Login / signup is just not ideal. Its clunky and gives very little user response. 

- Alot of little things missing like confirmation of copy to clipboard, confirmation of login, confirmation of signup, login errors, save errors, saving without a name ect. 


# Python
- I believe that the way my site functions in terms of user experience is flawd, there should be no reason for the page to reload every time someone requests a pallet and same goes for storing the pallet information. If you want to save but are no logged in you need to log in which then basically means you lose the pallet you were looking at initially which is not ideal 


# CSS
- Had a hard time creating flexible ways to display the colour information. Resorted to using purely RGB codes. 

- Navigation was a difficult task as the bar doesnt really suit pages other than the home page as it was designed around the bars of colour. 



