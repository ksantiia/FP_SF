import os

from dotenv import load_dotenv

load_dotenv()

valid_email = os.getenv('valid_email')
valid_password = os.getenv('valid_password')
valid_phone = os.getenv('valid_phone')
valid_login = os.getenv('valid_login')
valid_ls = os.getenv('valid_ls')
valid_firstname = os.getenv('valid_firstname')
valid_lastname = os.getenv('valid_lastname')
lat_firstname = os.getenv('lat_firstname')  # Имя записанное латиницей
lat_lastname = os.getenv('lat_lastname')   # Фамилия записанная латиницей