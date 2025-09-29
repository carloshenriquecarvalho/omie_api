from src.extract.api_client import call_omie_api

def fetch_all_sellers():

    print('Extraindo Vendedores...')
    page = 1
    all_sellers = []
    while True:
        params = [{
            "pagina": 1,
            "registros_por_pagina": 100,
            "apenas_importado_api": "N"
        }]
        response = call_omie_api(resource='geral/vendedores/', call='ListarVendedores', params=params)

        if response and response.get("cadastro"):
            all_sellers.extend(response["cadastro"])
            if page >= response.get("total_de_paginas", 0):
                break
            total_pages = response.get("total_de_paginas", 0)
            if page >= total_pages or not response:
                break
            page += 1
        else:
            print(f'({page}/{total_pages}) finalizados.')
            break
    return {"cadastro": all_sellers}