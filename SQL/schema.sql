DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS scenes;
DROP TABLE IF EXISTS saved_pallets;



CREATE TABLE users (
    id SERIAL PRIMARY KEY, 
    name VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    password_hash TEXT
);

CREATE TABLE scenes (
    id SERIAL PRIMARY KEY, 
    name VARCHAR(50) NOT NULL,
    image_url TEXT
);

CREATE TABLE saved_pallets (
    id SERIAL PRIMARY KEY, 
    color1 TEXT,
    color2 TEXT,
    color3 TEXT,
    color4 TEXT,
    color5 TEXT,
    user_id INTEGER,
    

    CONSTRAINT fk_website_user
        FOREIGN KEY (user_id)
         REFERENCES users(id)
);