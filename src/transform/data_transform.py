import pandas as pd

def transform_orders(json_data):
    print("Processin data...")
    if not json_data or not json_data.get("pedido_venda_produto"):
        print("No data to process.")
        return pd.DataFrame()

    df = pd.json_normalize(
        data=json_data["pedido_venda_produto"],
        record_path=['det'],
        meta= [
            ["cabecalho", "codigo_cliente"],
	        ["cabecalho", "codigo_pedido"],
	        ["cabecalho", "numero_pedido"],
            ["infoCadastro", "dInc"],
            ['infoCadastro', 'cancelado'],
            ['infoCadastro', 'dCan']
        ],
        sep="_",
        errors='ignore'
    )
    column_map = {
        "cabecalho_codigo_cliente": "id_cliente",
        "cabecalho_codigo_pedido": "id_pedido",
        "cabecalho_numero_pedido": "numero_pedido",
        "produto_codigo_produto": "id_produto",
        "produto_valor_unitario": "valor_unitario",
        "infoCadastro_dInc": "data_inclusao",
        "infoCadastro_cancelado": "status_cancelado",
        "infoCadastro_dCan": "data_cancelamento"
    }

    cols_to_keep = [col for col in column_map.keys() if col in df.columns]
    df_filtered = df[cols_to_keep]
    df_renamed = df_filtered.rename(columns=column_map)

    df_renamed['data_inclusao'] = pd.to_datetime(df_renamed['data_inclusao'], format='%d/%m/%Y', errors='coerce')
    if 'data_cancelamento' in df_renamed.columns:
        df_renamed['data_cancelamento'] = pd.to_datetime(df_renamed['data_cancelamento'], format='%d/%m/%Y', errors='coerce')

    df_renamed['valor_unitario'] = pd.to_numeric(df_renamed['valor_unitario'], errors='coerce')

    print(f"Transformação concluida. Tabela criada com {len(df_renamed)} linhas.")
    return df_renamed

def transform_sellers(json_data):
    print("Processin data...")
    if not json_data or not json_data.get("cadastro"):
        print("No data to process.")
        return pd.DataFrame()
    
    df = pd.json_normalize(json_data['cadastro'])
    column_map = {
        "codigo": "id_vendedor",
        "nome": "nome_vendedor",
        "inativo": "status_inativo"
    }

    cols_to_keep = [col for col in column_map.keys() if col in df.columns]
    df_filtered = df[cols_to_keep]
    df_renamed = df_filtered.rename(columns=column_map)
    print(f"Sellers transformation complete. DataFrame created with {len(df_renamed)} rows.")
    return df_renamed

def transform_products(json_data):
    print("Processando dados...")

    # Verifica se veio algo no JSON
    if not json_data or not json_data.get("produto_servico_cadastro"):
        print("Não há dados.")
        return pd.DataFrame()
    
    # Normaliza para DataFrame
    df = pd.json_normalize(json_data['produto_servico_cadastro'])

    # Mapeamento das colunas desejadas
    column_map = {
        'codigo_produto': 'id_produto',
        'descricao': 'descricao_produto',
        'valor_unitario': 'valor_unitario',
    }

    # Garante que só pega colunas existentes
    cols_to_keep = [col for col in column_map.keys() if col in df.columns]
    
    if not cols_to_keep:
        print("Nenhuma das colunas esperadas foi encontrada no JSON.")
        return pd.DataFrame()

    # Filtra e renomeia
    df_filtered = df[cols_to_keep].copy()
    df_renamed = df_filtered.rename(columns=column_map)

    print(f"Tranformação dos dados concluída e retornou {len(df_renamed)} linhas.")
    return df_renamed

def transform_clients(json_data):
    print("Processin data...")
    if not json_data or not json_data.get("clientes_cadastro"):
        print("No data to process.")
        return pd.DataFrame()
    
    df = pd.json_normalize(json_data['clientes_cadastro'])
    column_map = {
        'cidade': 'cidade_cliente',
        'codigo_cliente_omie': 'id_cliente',
        'nome_fantasia': 'nome_fantasia_cliente',
    }

    cols_to_keep = [col for col in column_map.keys() if col in df.columns]
    df_filtered = df[cols_to_keep]
    df_renamed = df_filtered.rename(columns=column_map)
    
    print(f"Transformação concluida. Tabela criada com {len(df_renamed)} linhas.")
    return df_renamed