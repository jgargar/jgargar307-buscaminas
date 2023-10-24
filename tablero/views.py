from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'tablero/index.html', {})

def crea_tablero(request):
    return render(request, 'tablero/crea_tablero.html', {})

def tablero(request):
    num1 = int(request.GET['fila'])
    num2 = int(request.GET['columna'])
    result = num1 + num2
    return render(request, 'tablero/tablero.html', {'result':result})