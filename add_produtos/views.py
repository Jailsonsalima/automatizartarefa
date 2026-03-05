from django.shortcuts import render, redirect
from usuarios.models import Usuario
from .models import Produto

# Create your views here.
def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        senha = request.POST.get("senha")

        # cria usuário se não existir
        usuario, created = Usuario.objects.get_or_create(email=email, senha=senha)
        request.session["usuario_id"] = usuario.id
        return redirect("produtos")  # vai para a segunda página

    return render(request, "add_produtos/login.html")

def produtos_view(request):
    usuario_id = request.session.get("usuario_id")
    usuario = Usuario.objects.get(id=usuario_id)

    if request.method == "POST":
        Produto.objects.create(
            usuario=usuario,
            codigo=request.POST.get("codigo"),
            marca=request.POST.get("marca"),
            tipo=request.POST.get("tipo"),
            categoria=request.POST.get("categoria"),
            preco=request.POST.get("preco"),
            custo=request.POST.get("custo"),
            obs=request.POST.get("obs"),
        )

    produtos = Produto.objects.filter(usuario=usuario)
    return render(request, "add_produtos/produtos.html", {"produtos": produtos})