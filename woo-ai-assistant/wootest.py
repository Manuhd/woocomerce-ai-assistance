import requests
from requests.auth import HTTPBasicAuth

url = "http://ecomerce-agentic-ai.local/wp-json/wc/v3/products"

consumer_key = "ck_8f6b99a774aed822c10549132fa9f05cf1dfb119"
consumer_secret = "cs_d38a8071cdc97e77d3418ecacc61066d0ef5f010"

response = requests.get(url, auth=HTTPBasicAuth(consumer_key, consumer_secret))

if response.status_code == 200:
    print(response.json())
else:
    print("Error:", response.status_code, response.text)
