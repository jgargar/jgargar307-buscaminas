from django.shortcuts import render

# Create your views here.

def crea_tablero(request):
    return render(request, 'tablero/crea_tablero.html', {})
