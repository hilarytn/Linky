-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS linky_test_db;
CREATE USER  IF NOT EXISTS 'linky_test'@'localhost' IDENTIFIED BY 'linky_dev_pwd@June2023';
GRANT ALL PRIVILEGES ON `linky_test_db`.* TO 'linky_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'linky_test'@'localhost';
FLUSH PRIVILEGES;
