from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def hanna(request):
#      return HttpResponse("<h1>hi im hanna</h1>")

# def jumua(request):
#     return HttpResponse("<h1>hi im jumua</h1>")

def names(request):
    name='any_name'
    list_of_names=['dan','jumua','hana']
    return render(request,'name.html',{'name_of_user': name})


# def name (request, name):
#     list_of_names=['dan','jumua','hana']
#     if name in list_of_names:
#         return HttpResponse(f'hi {name}')
#     else:
#         return HttpResponse(f'{name} is not in the list')

def subjects(request):
    list_of_subjects = ('math', 'Science', 'biology')
    return render(request, 'subjectlist.html',{'subjects':list_of_subjects})