-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS linky_dev_db;
CREATE USER  IF NOT EXISTS 'linky_dev'@'localhost' IDENTIFIED BY 'linky_dev_pwd@June2023';
GRANT ALL PRIVILEGES ON `linky_dev_db`.* TO 'linky_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'linky_dev'@'localhost';
FLUSH PRIVILEGES;
