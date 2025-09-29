from src.extract import orders, clients, products, sellers
from src.transform import data_transform
import gspread
import pandas as pd
import src.config

df = orders.fetch_all_orders()

