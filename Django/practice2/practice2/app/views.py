from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
names = ['adam', 'dude', 'lebawskey']
def named(request):
    return HttpResponse('hidden wazza planet')

def word(request):
    return HttpResponse('hi')

def great(request, name):
    names.append(name)
    return HttpResponse(f'hello {names} 'f' hello {name}')


def index(request, name):
    names.append(name)
    return render(request,'name.html',{'value':names})
def courses(request):
    return render(request,'courses.html')
def classes (request):
    if request.method == "POST":
        named = request.POST.get('name')
        names.append(named)
    return render(request,'class.html',{'value':names})
def press(request):
    return render(request,'press.html')