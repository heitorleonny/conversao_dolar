from django.shortcuts import render
import requests

""" 
Criar site onde mostra a cotação do dólar em tempo real e em que é possível converter um valor de reais pra dólares
 """


def index(request):
    valor_dolar = buscar_valor_dolar()
    context = {'valor_dolar': valor_dolar}
    

    return render(request, 'home/index.html', context)

def conversao(request):
    valor_dolar = buscar_valor_dolar()
    try:
        valor_usuario = (request.POST.get('valor'))
        valor_usuario = valor_usuario.replace(',', '.')
        valor_usuario = float(valor_usuario)
        conversao = round((valor_usuario / valor_dolar), 2)

        context = {'valor_usuario': valor_usuario, 'valor_dolar': valor_dolar, 'conversao': conversao}
        return render(request, 'home/index.html', context)
    
    except:
        valor_usuario = 'Valor inválido!'
        context = {'valor_usuario': valor_usuario, 'valor_dolar': valor_dolar}
        return render(request, 'home/index.html', context)


def buscar_valor_dolar():
    response = requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL')
    if response.status_code == 200:
        url = response.json()
        dolar = url['USDBRL']
        valor_dolar = float(dolar['bid'])
        return round(valor_dolar, 2)