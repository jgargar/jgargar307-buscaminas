from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'tablero/index.html', {})

def crea_tablero(request):
    return render(request, 'tablero/crea_tablero.html', {})

def tablero(request):
    tabla = [[f'Fila {i}, Celda {j}' for j in range(1, int(request.GET['columna']) + 1)] for i in range(1, int(request.GET['fila']) + 1)]
    return render(request, 'tablero/tablero.html', {'tabla':tabla})