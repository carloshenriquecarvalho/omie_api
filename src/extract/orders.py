from src.extract.api_client import call_omie_api
from datetime import datetime
from dateutil.relativedelta import relativedelta # Ótima biblioteca para manipular datas

def get_monthly_periods(start_date_str):
    """
    Gera uma lista de períodos (início e fim de cada mês)
    a partir de uma data de início até o mês atual.
    """
    periods = []
    current_date = datetime.strptime(start_date_str, '%d/%m/%Y')
    end_date = datetime.now()

    while current_date <= end_date:
        # Define o início do mês
        start_of_month = current_date.strftime('%d/%m/%Y')
        # Define o fim do mês
        end_of_month = (current_date + relativedelta(months=1, days=-1)).strftime('%d/%m/%Y')
        
        periods.append({'start': start_of_month, 'end': end_of_month})
        
        # Vai para o primeiro dia do próximo mês
        current_date += relativedelta(months=1)
        
    return periods

def fetch_all_orders():
    """
    Busca todos os pedidos da API, quebrando a busca em períodos mensais
    para evitar sobrecarga e erros no servidor.
    """
    print("Extraindo dados de mês a mês a partir de 01/01/2025...")
    
    start_date = "01/01/2025" # Mantenha o início do ano
    monthly_periods = get_monthly_periods(start_date)
    
    all_orders = []

    # Loop através de cada período mensal (Janeiro, Fevereiro, etc.)
    for period in monthly_periods:
        print(f"\n--- Extraindo da data: {period['start']} até {period['end']} ---")
        page = 1
        
        while True:
            # Filtra por data de início E data de fim para cada mês
            params = [{
                "pagina": page, 
                "registros_por_pagina": 100,
                "filtrar_por_data_de": period['start'],
                "filtrar_por_data_ate": period['end']
            }]
            
            response = call_omie_api("produtos/pedido/", 'ListarPedidos', params)
            
            if response and response.get("pedido_venda_produto"):
                all_orders.extend(response["pedido_venda_produto"])
                total_pages = response.get("total_de_paginas", 0)
                
                if total_pages == 0: # Caso especial para meses sem pedidos
                    print("No orders found for this period.")
                    break
                
                print(f'Página {page} de {total_pages} do período conlcluída.')
                
                if page >= total_pages:
                    break
                page += 1
            else:
                # Se a API falhar para este mês, o loop para e vai para o próximo mês
                print(f"Falhou ao tentar recolher os dados deste período. Pulando para o próximo.")
                break
                
    print(f"\nFinished extracting all periods. Total orders found: {len(all_orders)}")
    return {"pedido_venda_produto": all_orders}