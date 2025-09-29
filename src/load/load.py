

import gspread

def load_to_sheets(df, sheet_name, worksheet_name="Página1"):
    """
    Carrega um DataFrame para uma aba no Google Sheets
    mantendo o cabeçalho (linha 1).
    """
    # 1. Autenticar
    gc = gspread.service_account()

    # 2. Abrir planilha e worksheet
    sh = gc.open(sheet_name)
    sheet = sh.worksheet(worksheet_name)

    # 3. Transformar DataFrame em lista de listas
    dados = df.values.tolist()
    dados.insert(0, df.columns.tolist())  # adiciona cabeçalho

    # 4. Limpar apenas os dados (mantém linha 1 fixa)
    ultima_coluna = chr(64 + len(df.columns))  # ex: 3 colunas -> 'C'
    sheet.batch_clear([f"A2:{ultima_coluna}"])

    # 5. Atualizar
    sheet.update("A1", dados)

    print("✅ Dados carregados com sucesso no Google Sheets!")