#!/bin/bash

mysql -u root -e "CREATE DATABASE asterisk"
mysql -u root -e "CREATE USER 'asteriskuser'@'localhost' IDENTIFIED BY 'password'"
mysql -u root -e "GRANT ALL PRIVILEGES ON asterisk.* TO 'asteriskuser'@'localhost'"
mysql -u root -e "FLUSH PRIVILEGES"