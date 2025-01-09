#!/bin/bash

echo "Instalando dependências"
apt-get update
apt-get install python3-venv mysql-server -y

echo "Copiando arquivos de configuração do Asterisk"
cp -a config/conf/* /etc/asterisk/

echo "Configurando mysql"
mysql -u root -e "CREATE DATABASE asterisk"
mysql -u root -e "CREATE USER 'asteriskuser'@'localhost' IDENTIFIED BY 'password'"
mysql -u root -e "GRANT ALL PRIVILEGES ON asterisk.* TO 'asteriskuser'@'localhost'"
mysql -u root -e "FLUSH PRIVILEGES"
mysql -u root asterisk < config/sql/asterisk.sql

echo "Criando VENV"
python3 -m venv venv

echo "Instalando dependências"
source venv/bin/activate
pip install -r src/requirements.txt

echo "Configurando serviço"
cp config/systemd/wpp-send.service /etc/systemd/system/
systemctl enable wpp-send
systemctl daemon-reload
systemctl start wpp-send.service