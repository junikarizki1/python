from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context ={
        'title':'Home Pages',
        'welcome':'Welcome to Home Page',
        'desc':'Ini website halal'
    }
    return render(request,'index.html', context)

def about(request):
    context ={
        'title':'About Page',
        'welcome':'Welcome to About Page',
        'desc':'Ini website halal'
    }
    return render(request,'about.html', context)

def news(request):
    return HttpResponse("<h1>Belajar Menggunakan Views dan Template<h1/>")