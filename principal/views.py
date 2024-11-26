from django.shortcuts import render

# Create your views here.

def findex(request):
    return render(request, "index.html")

def fhistoria(request):
    return render(request, "historia.html")

def fcelulares(request):
    return render(request, "celulares.html")

def fcapinhas(request):
    return render(request, "capinhas.html")

def facessorios(request):
    return render(request, "acessorios.html")

def flogin(request):
    return render(request, "login.html")
