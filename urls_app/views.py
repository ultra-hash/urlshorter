from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World")


def short(request, shorturl):
    return HttpResponse("<h1>Hello "+ shorturl +"</h1>")