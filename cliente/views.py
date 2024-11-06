from django.shortcuts import render
from .models import Cliente
# Create your views here.
def fcliente(request):
    clientes = Cliente.objects.all()
    return render(request, "cad_cliente.html", {"clientes": clientes})

