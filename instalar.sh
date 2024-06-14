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
apt-get update || error_exit "Error al actualizar el sistema"
apt-get upgrade -y || error_exit "Error al actualizar los paquetes"

# Instalar dependencias
echo "Instalando dependencias..."
apt-get install -y curl wget git || error_exit "Error al instalar dependencias"

echo "Instalando git"
apt-get install git
# Verificar si python3 está instalado
if command -v python3 &> /dev/null
then
    echo "python3 ya está instalado"
else
    echo "instalando python3"
    sudo apt-get install -y python3 || error_exit "Error al instalar python3"
fi


echo "Instalando pip"
sudo apt-get install python3-pip || error_exit "Error al instalar pip"

echo "Instalando flask"
pip3 install Flask || error_exit "Error al instalar flask"

# Instalar PyMySQL
echo "Instalando PyMySQL..."
pip3 install PyMySQL || error_exit "Error al instalar PyMySQL"
echo "Instalación completada con éxito"

echo "instalando spacy"
pip install spacy

echo "descargando modelos"
python -m spacy download es_core_news_sm

echo "instalando numpy"
pip install numpy

echo "instalando sentence transformers"
pip install sentence-transformers
