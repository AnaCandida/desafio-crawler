CREATE TABLE IF NOT EXISTS movies (
    id SERIAL PRIMARY KEY,
    rank INTEGER UNIQUE,
    title VARCHAR(255),
    stars FLOAT,
    year INTEGER,
    duration VARCHAR(255)

);