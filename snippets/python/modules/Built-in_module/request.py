import requests

url = 'http://172.31.2.237:9100'

response = requests.get(url)
print(response.status_code)
print(response.text)
