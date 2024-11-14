from django.shortcuts import render, redirect
from .models import Produto
# Create your views here.
def fproduto(request):
    produtos = Produto.objects.all()
    return render(request, "rel_produto.html", {"produtos": produtos})

def fcadproduto(request):
        return render(request, "cad_produto.html")

def salvar(request):
    vmarca = request.POST.get("marca")
    vdescricao = request.POST.get("descricao")
    vpreco = request.POST.get("preco")
    vquantidade = request.POST.get("quantidade")
    vimagem = request.FILES.get("imagem")

    if vmarca:
        Produto.objects.create(marca=vmarca,
                               descricao=vdescricao,
                               preco=vpreco,
                               quantidade=vquantidade,
                               imagem=vimagem
                               )
    return redirect(fproduto)


def exibir(request, id):
    produto = Produto.objects.get(id=id)
    return render(request, "update.html", {"produto": produto})


def excluir(request, id):
    produto = Produto.objects.get(id=id)
    produto.delete()
    return redirect(fproduto)

def update(request, id):
    vmarca = request.POST.get("marca")
    vdescricao = request.POST.get("descricao")
    vpreco = request.POST.get("preco")
    vquantidade = request.POST.get("quantidade")
    vimagem = request.FILES.get("imagem")
    produto = Produto.objects.get(id=id)
    produto.marca = vmarca
    produto.descricao = vdescricao
    produto.preco = vpreco
    produto.quantidade = vquantidade
    if vimagem:
        produto.imagem = vimagem
    produto.save()
    return redirect(fproduto)
