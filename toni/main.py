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

    print (f'El teu nom és {user_name}, "Usuari"')
    #ALERTA! conflicte amb la branca develop
    print(f'El teu nom és {user_name}')
    
    # HTML amb el missatge personalitzat
    html_content = f"""
    <!DOCTYPE html>
    <html>
        <head>
            <title>Benvingut</title>
        </head>
        <body>
            <h1>Hola {user_name}, estàs utilitzant FastAPI</h1>
            <p> You are welcome</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)