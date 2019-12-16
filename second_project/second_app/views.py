from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def home(request):
#     return HttpResponse("Hello World")

def index(request):
    my_dict={'insert_me':"Hello i am from views.py"}
    return render(request,'second_app/index.html',context=my_dict)
