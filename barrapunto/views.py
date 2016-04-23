from django.shortcuts import render
from django.http import HttpResponse
from bp import get_fich
from models import Pages
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def listar(request):
    Lista = Pages.objects.all()
    response = "<ol>"
    for page in Lista:
        response += "<li><a href = '/"+ str(page.id) +"'>"+page.name + "</a>"
    response += "</ol>"
    return HttpResponse(response)

def insertar(request,name,page):
    newpage = Pages(name = name, page=page)
    newpage.save()
    response="200 OK"
    return HttpResponse(response)

def mostrar(request, identificador):
    try:

        barrapunto = get_fich(identificador)
        page = Pages.objects.get(id=identificador)
        response = page.page +'<br>'+ page
    except ObjectDoesNotExist:
        response = "Does not exist"
    return HttpResponse(response)
