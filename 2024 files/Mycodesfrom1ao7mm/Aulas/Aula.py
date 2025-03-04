import requests
site = 'https://viasep.com.br/ws/15806080/'
result = requests.get(url=site)
print(result.text)