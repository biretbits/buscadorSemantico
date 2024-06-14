#!/bin/bash

# Función para mostrar mensajes de error y salir
error_exit() {
    echo "$1" >&2
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

# Instalar git
echo "Instalando git..."
sudo apt install -y git || error_exit "Error al instalar git"

# Verificar si python3 está instalado
if ! command -v python3 &> /dev/null; then
    echo "Instalando python3..."
    sudo apt install -y python3 || error_exit "Error al instalar python3"
else
    echo "python3 ya está instalado"
fi

# Instalar pip
echo "Instalando pip..."
sudo apt install -y python3-pip || error_exit "Error al instalar pip"

# Instalar Flask
echo "Instalando Flask..."
sudo pip3 install Flask || error_exit "Error al instalar Flask"

# Instalar PyMySQL
echo "Instalando PyMySQL..."
sudo pip3 install PyMySQL || error_exit "Error al instalar PyMySQL"
echo "Instalación completada con éxito"

# Instalar spacy y descargar modelos
echo "Instalando spacy y descargando modelos..."
sudo pip install spacy || error_exit "Error al instalar spacy"
python -m spacy download es_core_news_sm || error_exit "Error al descargar modelos de spacy"

# Instalar numpy
echo "Instalando numpy..."
sudo pip install numpy || error_exit "Error al instalar numpy"

# Instalar sentence-transformers
echo "Instalando sentence-transformers..."
sudo pip install sentence-transformers || error_exit "Error al instalar sentence-transformers"

echo "Todo ha sido instalado correctamente"
