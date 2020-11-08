from django.http import HttpResponse
from pro10.models import Article
from django.shortcuts import render

def saludo(request):#primer vbuista
    return HttpResponse("hola colegas a meter codigo duro y bueno")
#//segunda vista
def  despedida(request):
    return HttpResponse("esdta luego angel")
    #//devolver e lonjeto hhtpresponse y como parametro el pasamos 
    
    


def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'news/year_archive.html', context)