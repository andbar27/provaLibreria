#!/bin/bash

# Porta su cui avviare Django
PORT=8000

echo $(hostname -I)

echo "Avvio del progetto Django..."

cd /home/salotto/proj/provaLibreria || { echo "Cartella non trovata!"; exit 1; }

# Avviare il server Django
echo "Avvio del server Django su http://127.0.0.1:$PORT/"
python3 manage.py runserver 0.0.0.0:$PORT

