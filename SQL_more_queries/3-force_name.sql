-- CREATE a table that will force the name column to never fail
CREATE TABLE IF NOT EXISTS force_name(id INT,name VARCHAR(256) NOT NULL);
