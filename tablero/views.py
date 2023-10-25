from django.shortcuts import render

from tablero.forms import crearTableroForms


# Create your views here.

def index(request):
    return render(request, 'tablero/index.html', {})

def crea_tablero(request):
    formulario = crearTableroForms()
    # Si se ha enviado el formulario
    if request.method == "GET":
        formulario = crearTableroForms(request.GET or None)
        #Ejecutamos la validacion
        if formulario.is_valid():
            columnas = formulario.cleaned_data['columnas'] #Sitio de donde se cogen los valores validados
            filas = formulario.cleaned_data['filas']
            return render(request, 'tablero/tablero.html',
                          {'filas': filas, 'columnas': columnas,
                           'rango_filas':range(filas), 'rango_columnas': range(columnas)})
    #Si se se pide la pagina por primera vez
    return render(request, 'tablero/crea_tablero.html', {'form':formulario})

'''
def tablero(request):
    tabla = [[f'{i}, {j}' for j in range(1, int(request.GET['columnas']) + 1)] for i in range(1, int(request.GET['filas']) + 1)]
    return render(request, 'tablero/tablero.html', {'tabla':tabla})
'''