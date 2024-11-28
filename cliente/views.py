from django.shortcuts import render, redirect
from .models import Cliente
from django.contrib.auth.hashers import make_password
from django.contrib import messages
# Create your views here.
def fcliente(request):
    clientes = Cliente.objects.all()
    return render(request, "rel_cliente.html", {"clientes": clientes})

def fcadcliente(request):
    return render(request, "cad_cliente.html")

def salvar_cliente(request):
    vnome = request.POST.get("nome")
    vtelefone = request.POST.get("telefone")
    vemail = request.POST.get("email")
    vsenha = request.POST.get("senha")

    senha_criptografada = make_password(vsenha)
    if vnome:
        Cliente.objects.create(nome=vnome, telefone=vtelefone, email=vemail, senha=senha_criptografada)
    return redirect(fcliente)

def exibir_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    return render(request, 'update_cliente.html', {"cliente": cliente})

def excluir_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect(fcliente)

def update_cliente(request, id):
    vnome = request.POST.get("nome")
    vtelefone = request.POST.get("telefone")
    vemail = request.POST.get("email")
    cliente = Cliente.objects.get(id=id)
    cliente.nome = vnome
    cliente.telefone = vtelefone
    cliente.email = vemail
    cliente.save()
    return redirect(fcliente)

def flogin(request):
    return render(request, "login.html")


def logar(request):
    if request.method == 'POST':
        # Correção do nome do campo para 'email' ao invés de 'username'
        email = request.POST.get('email')
        senha = request.POST.get('password')

        try:
            cliente = Cliente.objects.get(email=email)
            if cliente.check_password(senha):
                return redirect('telacli')  # Redireciona para a tela principal após login bem-sucedido
            else:
                # Mensagem de erro caso a senha esteja incorreta
                messages.error(request, 'Senha inválida.')
                return redirect('flogin')  # Redireciona para a página de login
        except Cliente.DoesNotExist:
            # Mensagem de erro caso o cliente com o email não seja encontrado
            messages.error(request, 'Credenciais inválidas.')
            return redirect('flogin')  # Redireciona para a página de login



def telacli(request):
    return render(request, "telacliente.html")


