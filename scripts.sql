-- Create database.
CREATE DATABASE camiones CHARACTER SET utf8;

-- Create table.
USE camiones;
CREATE TABLE count_passengers (
  id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  reg_date TIMESTAMP
);

-- Insert a data in count_passengers tables.
INSERT INTO count_passengers (reg_date) VALUES ('2018-03-26 23:33:11');

-- Select all values from count_passengers table.
SELECT id, reg_date FROM count_passengers;