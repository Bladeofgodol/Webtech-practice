from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<a href='http://127.0.0.1:8000/polls/2'><h1>Hello world 1</h1></a>")
# Create your views here.
def index2(request):
    return HttpResponse("<a href='http://127.0.0.1:8000/polls/3'><h1>Hello world 2</h1></a>")
def index3(request):
    return HttpResponse("<a href='http://127.0.0.1:8000/polls/4'><h1>Hello world 3</h1></a>")
def index4(request):
    return HttpResponse("<a href='http://127.0.0.1:8000/polls/'><h1>Hello world 4</h1></a>")
