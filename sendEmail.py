import requests
from dotenv import load_dotenv
import os

def call_api():
    load_dotenv()

    url = "https://wigaapimanagement.azure-api.net/deploymentEmail/correo?despliegue={}".format(os.getenv("DEPLOYMENT"))
    headers = {
        "Ocp-Apim-Subscription-Key": os.getenv("SUBSCRIPTION_KEY"),
        "id": os.getenv("ID"),
    }
    body = {
        "asunto": "Actualización Wigaming since SCRIPT EN PYTHON",
        "destinatarios": [ "sneider.caicedo@gmail.com" ],
        "backlog": os.getenv("BACKLOG")
    }

    try:
        response = requests.post(url, headers=headers, json=body)
        print("Status Code {} --> Successfully {} ".format(response.status_code, response.json()))
    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))

call_api()