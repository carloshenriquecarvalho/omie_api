from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='src/.env')

BASE_URL = os.getenv("BASE_URL")
APP_KEY = os.getenv("APP_KEY")
APP_SECRET = os.getenv("APP_SECRET")