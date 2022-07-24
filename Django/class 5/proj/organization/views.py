from django.shortcuts import get_object_or_404, render
from requests import request
from .models import Catagory,Post

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def service(request):
    return render(request)

def contact(request):
    return render(request,'contact.html')

def blog(request):
    news = Post.objects.all()
    return render(request,'blog.html',{'news': news})

def blogdetail(request,id):
    news =get_object_or_404(Post,id = id)
    return render(request,'blog-single.html',{'news': news})
    
# Create your views here.
