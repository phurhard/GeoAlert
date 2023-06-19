-- Prepares a mysql database for the project 
CREATE DATABASE IF NOT EXISTS GeoAlert;
CREATE USER IF NOT EXISTS 'admin'@'localhost' IDENTIFIED BY 'GeoAlertAdmin';
GRANT ALL PRIVILEGES ON `GeoAlert`.* TO 'admin'@'localhost';
FLUSH PRIVILEGES;
