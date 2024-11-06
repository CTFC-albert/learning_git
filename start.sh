#!/bin/bash

# Comprovar si s'ha proporcionat un argument (nom de la carpeta)
if [ $# -eq 0 ]; then
    echo "Error: Si us plau, proporciona el nom de la carpeta"
    echo "Ús: ./start.sh nom_carpeta"
    exit 1
fi

FOLDER_NAME=$1

# Comprovar si existeix la carpeta
if [ ! -d "$FOLDER_NAME" ]; then
    echo "Error: La carpeta $FOLDER_NAME no existeix"
    exit 1
fi

# Comprovar si existeix requirements.txt dins la carpeta del projecte
if [ ! -f "${FOLDER_NAME}/requirements.txt" ]; then
    echo "Error: No s'ha trobat l'arxiu requirements.txt dins la carpeta ${FOLDER_NAME}"
    exit 1
fi

# Crear i activar entorn virtual
echo "Creant entorn virtual..."
python -m venv venv
source venv/bin/activate

# Instal·lar dependències
echo "Instal·lant dependències..."
pip install -r ${FOLDER_NAME}/requirements.txt

# Executar l'aplicació
echo "Iniciant l'aplicació..."
uvicorn ${FOLDER_NAME}.main:app --reload