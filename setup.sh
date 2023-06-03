#! /usr/bin/env bash

echo 'Buscando python 3...'


sudo apt install python3 -y
sudo apt install python3-pip -y

echo 'PYTHON 3 INSTALADO'

echo 'Instalando bibliotecas necessárias...'


pip3 install -r ./requirements.txt

echo ''
echo 'TODAS AS BIBLIOTECAS INSTADAS'
echo ''




