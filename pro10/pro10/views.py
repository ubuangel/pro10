from django.http import HttpResponse
from _datetime import datetime

def saludo(request):#primer vbuista
    return HttpResponse("<html><body><h1>hola colegas a meter codigo duro y bueno</h1></body></html>")
#//segunda vista
def  despedida(request):
    return HttpResponse("esdta luego angel")
    #//devolver e lonjeto hhtpresponse y como parametro el pasamos 
def dameFecha(request):
    fecha_actual=datetime.datetime.now()
    #type object 'datetime.datetime' has no attribute 'datetime'    
    documento="""<html><bosy><h1> Fecha y hora actuales %s</html></bosy></h1>"---%fecha_actual"""%fecha_actual
        
    return HttpResponse(documento)