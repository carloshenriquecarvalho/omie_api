from src.extract.api_client import call_omie_api

def fetch_all_products():
    print("Extraindo produtos...")
    page = 1
    all_products = []

    while True:
        params = [{
            "pagina": page,
            "registros_por_pagina": 100, 
            "apenas_importado_api": "N",
            "filtrar_apenas_omiepdv": "N"
        }]

        response = call_omie_api(resource="geral/produtos/", call="ListarProdutos", params=params)

        if response and "produto_servico_cadastro" in response:
            produtos_da_pagina = response.get("produto_servico_cadastro", [])
            all_products.extend(produtos_da_pagina)

            total_pages = response.get("total_de_paginas", 0)
            print(f'({page}/{total_pages}) finalizados.')

            if page >= total_pages:
                break
            
            page += 1
        else:
            print("Sem produtos ou ocorreu um erro com a API.")
            break

    
    return {"produto_servico_cadastro": all_products}