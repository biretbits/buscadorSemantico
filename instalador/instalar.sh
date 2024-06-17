#!/bin/bash

# Función para mostrar mensajes de error y salir
error_exit() {
    echo "$1" 1>&2
    exit 1
}

# Verificar si el script se está ejecutando como root
if [ "$(id -u)" != "0" ]; then
    error_exit "Ejecute con root"
fi
# Actualizar el sistema
echo "Actualizando el sistema..."
sudo apt update || error_exit "Error al actualizar el sistema"
sudo apt upgrade -y || error_exit "Error al actualizar los paquetes"

# Instalar dependencias
echo "Instalando dependencias..."
sudo apt install -y curl wget git || error_exit "Error al instalar dependencias"

echo "Instalando git"
sudo apt install git

echo "instalando python3"
sudo apt install -y python3 || error_exit "Error al instalar python3"



echo "Instalando pip"
sudo apt install python3-pip || error_exit "Error al instalar pip"

echo "Instalando flask"
sudo pip3 install Flask || error_exit "Error al instalar flask"

pip install weasyprint
sudo apt update
sudo apt install libpango1.0-0
pip install flask-session

# Instalar PyMySQL
echo "Instalando PyMySQL..."
sudo pip3 install PyMySQL || error_exit "Error al instalar PyMySQL"
echo "Instalación completada con éxito"

echo "instalando spacy"
sudo pip install spacy

echo "descargando modelos"
python3 -m spacy download es_core_news_sm

echo "instalando numpy"
sudo pip install numpy
