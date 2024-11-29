from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from dotenv import load_dotenv
import os

# Carregar variables d'entorn
load_dotenv()

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    # Obtenir el nom d'usuari del .env
    user_name = os.getenv("USER_NAME", "Usuari")
    #ALERTA! conflicte amb la branca develop
    print(f'El teu nom és {user_name}')
    print(f'Avui segur que funciona tot a la primera x-D')
    
    # HTML amb el missatge personalitzat
    html_content = f"""
    <!DOCTYPE html>
    <html>
        <head>
            <title>Benvingut</title>
        </head>
        <body>
            <h1>Hola {user_name}, estàs utilitzant FastAPI</h1>
            <p>Ostres! aquí no també ens indica un conflicte</p>
            <footer>
                <p>Aquí no ens indica cap conflicte! Avui segur que funciona tot a la primera x-D</p>
            </footer>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)