import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key= os.getenv("CURRENCY_API")

url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"


requests = requests.get(url)
data = requests.json()

print(data)