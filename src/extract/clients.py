from .api_client import call_omie_api

def fetch_all_clients():
    # faz um fetch com os clientes que tem a tag cliente
    print("Extraindo Clientes...")
    page = 1
    all_clients = []
    while True:

        params = [{
            "pagina": page,
            "registros_por_pagina": 100
        }]

        response = call_omie_api(resource="geral/clientes/", call='ListarClientes', params=params)
        data = response
        
        clients = data.get('clientes_cadastro', [])
        
        # filtra clientes com a tag cliente
        filtered_clients = [
            client for client in clients
            if any(tag.get("tag") == "Cliente" for tag in client.get("tags", []))
        ]

        if filtered_clients:
            all_clients.extend(filtered_clients)

        total_pages = data.get("total_de_paginas", 0)
        if page >= total_pages or not clients:
            break
        print(f'({page}/{total_pages}) finalizados.')
        page += 1

    return {"clientes_cadastro": all_clients}