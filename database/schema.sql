CREATE DATABASE tourist_app;
USE tourist_app;

DROP USER IF EXISTS 'tourist_user'@'localhost';
FLUSH PRIVILEGES;

CREATE USER 'tourist_user'@'localhost' IDENTIFIED WITH mysql_native_password BY '22Rt_202*';
GRANT ALL PRIVILEGES ON *.* TO 'tourist_user'@'localhost';
FLUSH PRIVILEGES;

CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100),
  password VARCHAR(255)
);
