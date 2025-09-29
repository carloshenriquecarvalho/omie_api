import requests as r
from src import config

def call_omie_api(resource, call, params):
    # monta a URL correta
    full_url = f"{config.BASE_URL.rstrip('/')}/{resource.lstrip('/')}"

    payload = {
        "call": call,
        "app_key": config.APP_KEY,
        "app_secret": config.APP_SECRET,
        "param": params
    }

    headers = {"Content-Type": "application/json"}

    try:
        response = r.post(url=full_url, json=payload, headers=headers)
        response.raise_for_status()

        return response.json()
    except r.exceptions.RequestException as e:
        print(f"Comunicação com a API falhou. Call '{call}': '{e}'")
        return None
    except ValueError:
        print("Erro ao decodificar resposta da API. Conteúdo não é JSON.")
        return None