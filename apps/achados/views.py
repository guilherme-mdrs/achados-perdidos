from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import ObjetoForm
from .models import Objeto


def index(request):
    objetos = Objeto.objects.all().order_by("-created_at")

    return render(
        request,
        "achados/index.html",
        {"objetos": objetos},
    )


def cadastrar_objeto(request):
    if not request.user.is_authenticated:
        return redirect("achados:login")

    if request.method == "POST":
        form = ObjetoForm(request.POST, request.FILES)

        if form.is_valid():
            objeto = form.save(commit=False)
            objeto.usuario = request.user
            objeto.save()

            return redirect("achados:index")

    else:
        form = ObjetoForm()

    return render(
        request,
        "achados/cadastrar.html",
        {"form": form},
    )


def login_usuario(request):
    erro = None

    if request.method == "POST":
        email = request.POST.get("email")
        senha = request.POST.get("senha")

        usuario = authenticate(
            request,
            email=email,
            password=senha,
        )

        if usuario is not None:
            login(request, usuario)
            return redirect("achados:index")

        erro = "E-mail ou senha inválidos."

    return render(
        request,
        "achados/login.html",
        {"erro": erro},
    )


def logout_usuario(request):
    logout(request)
    return redirect("achados:index")