from django.shortcuts import render
import urllib.request
import json

# Create your views here.
def index(request):
    if request.method == 'POST':
        creature = request.POST['creature'].lower()
        creature = creature.replace(' ', '%20')
        url_api = urllib.request.Request('https://eldenring.fanapis.com/api/creatures&name={creature}')
        url_api.add_header('User-Agent', 'basilisk')
        
        source = urllib.request.urlopen(url_api).read()
        
        lista_datos = json.loads(source)
        
        datos = {
            'id': str(lista_datos['id']),
            'name': str(lista_datos['name']).capitalize(),
            'descripcion': str(lista_datos['description']).capitalize(),
            'imagen': str(lista_datos['image'])
        }
        
        print(datos)
    