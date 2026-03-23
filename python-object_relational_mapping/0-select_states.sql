-- Create database hbtn_0e_0_usa if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;

-- Use the database
USE hbtn_0e_0_usa;

-- Create states table if it doesn't exist
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);

-- Insert sample data into the states table
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");
