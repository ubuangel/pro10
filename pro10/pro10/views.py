from django.http import HttpResponse

def saludo(request):#primer vbuista
    return HttpResponse("hola colegas a meter codigo duro y bueno")
#//segunda vista
def  despedida(request):
    return HttpResponse("esdta luego angel")
    #//devolver e lonjeto hhtpresponse y como parametro el pasamos 