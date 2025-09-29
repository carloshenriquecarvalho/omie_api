from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente
load_dotenv(dotenv_path='src/dotenv_files/.env')

# Declara as variáveis de ambiente em constantes
BASE_URL = os.getenv("BASE_URL")
APP_KEY = os.getenv("APP_KEY")
APP_SECRET = os.getenv("APP_SECRET")