import requests

url = 'http://localhost:8080/2015-03-31/functions/function/invocations'
#data = {'url': 'https://upload.wikimedia.org/wikipedia/en/e/e9/GodzillaEncounterModel.jpg'}
data = {'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Smaug_par_David_Demaret.jpg/1280px-Smaug_par_David_Demaret.jpg'}
result = requests.post(url, json=data).json()

print(result)