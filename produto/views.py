from django.shortcuts import render
from .models import Produto
# Create your views here.
def fproduto(request):
    return render(request, "cad_produto.html", {"produto": Produto})