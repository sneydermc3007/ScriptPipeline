import requests

def call_api():
    url = "https://api-colombia.com/api/v1/Department"
    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        print('Información de los departamentos de Colombia: \n {}'.format(data))
        
    except requests.exceptions.RequestException as e:
        print("Error al llamar a la API:", e)

call_api()