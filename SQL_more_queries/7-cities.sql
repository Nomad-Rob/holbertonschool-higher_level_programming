--creates a database named hbtn_0d_usa containing a table named cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
use hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    state_id INT NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id),
    name VARCHAR(256) NOT NULL
);
