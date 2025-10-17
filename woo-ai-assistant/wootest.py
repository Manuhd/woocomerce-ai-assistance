import requests
from requests.auth import HTTPBasicAuth

url = "http://ecomerce-agentic-ai.local/wp-json/wc/v3/products"

consumer_key = "ck_xxxxxxxxxxxdfb119"
consumer_secret = "cs_xxxxxxxxx5f010"

response = requests.get(url, auth=HTTPBasicAuth(consumer_key, consumer_secret))

if response.status_code == 200:
    print(response.json())
else:
    print("Error:", response.status_code, response.text)

