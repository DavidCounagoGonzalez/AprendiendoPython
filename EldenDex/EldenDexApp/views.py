from django.shortcuts import render
import urllib.request
import json
from django.core.paginator import Paginator

# Create your views here.
def index(request, pagina):
    datos = {}
    if request.method == 'GET':
        url_api = urllib.request.Request('https://eldenring.fanapis.com/api/creatures?page=' + str(pagina))
        url_api.add_header('User-Agent', 'basilisk')
        
        source = urllib.request.urlopen(url_api).read()
        
        lista_datos = json.loads(source)
        
        datos = lista_datos['data']
        print(pagina)
    else:
        datos = {}
        
    return render(request, 'index.html', {'datos': datos, 'pagina': pagina})
