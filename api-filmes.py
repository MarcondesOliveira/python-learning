import requests
import json

req = None

nome = input('Digite o nome do filme\n')

try:
    req = requests.get("http://theapache64.xyz:8080/movie_db/search?keyword="+nome)
except:
    if req == False:
        print('Erro na conexão')
        exit()

dicionario = json.loads(req.text)

print('\n-Título:',dicionario['data'].get('name'))
print('-Atores:',dicionario['data'].get('stars'))
print('-Gênero:',dicionario['data'].get('genre'))
print('-Ano:',dicionario['data'].get('year'))
print('-Sinopse:',dicionario['data'].get('plot'))
print('-Poster:',dicionario['data'].get('poster_url'))
print('-Nota:',dicionario['data'].get('rating'))