from django.http import HttpResponse
from django.shortcuts import render

import datetime 

# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")
def sayhi(request):
    return HttpResponse("Hola con todos")
def sayhello(request, name):
    return HttpResponse(f"Hola con {name.capitalize()}")

def sayhellowithtemplate(request):
    return render(request,"hello/hola_mundo.html")

def sayhellotemplate(request, name):
    return render(request,"hello/withcontent.html",{"name":name.capitalize()})

def whatdayistoday(request):
    date = datetime.datetime.now()    
    return HttpResponse(date)

