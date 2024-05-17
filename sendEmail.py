import requests
from dotenv import load_dotenv
import os

def call_api():
    load_dotenv()

    url = "https://wigaapimanagement.azure-api.net/deploymentEmail/correo"
    payload = { "despliegue": "Wigaming" }
    headers = {
        "Ocp-Apim-Subscription-Key": os.getenv("SUBSCRIPTION_KEY"),
        "id": os.getenv("ID"),
    }
    body = {
        "asunto": "Actualización Wigaming since SCRIPT EN PYTHON",
        "destinatarios": [ "sneider.caicedo@gmail.com" ],
        "img": "https://wiscanstorage.blob.core.windows.net/pantillas-despliegues/wigaming.png"
    }

    try:
        response = requests.post(url, params=payload, headers=headers, json=body)
        print("Status Code {} --> Successfully {} ".format(response.status_code, response.json()))
    except requests.exceptions.RequestException as e:
        print("Status Code Error {}".format(response.status_code))
        print("Error en el envio del correo: ", e)

call_api()