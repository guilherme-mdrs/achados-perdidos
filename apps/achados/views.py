from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404

from .forms import CategoriaForm, LocalForm, ObjetoForm
from .models import Categoria, Local, Objeto


def index(request):
    objetos = Objeto.objects.all().order_by("-created_at")

    return render(
        request,
        "achados/index.html",
        {"objetos": objetos},
    )


#objetos
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


def editar_objeto(request, pk):
    if not request.user.is_authenticated:
        return redirect("achados:login")

    objeto = Objeto.objects.get(pk=pk)

    if request.method == "POST":
        form = ObjetoForm(
            request.POST,
            request.FILES,
            instance=objeto,
        )

        if form.is_valid():
            form.save()
            return redirect("achados:index")

    else:
        form = ObjetoForm(instance=objeto)

    return render(
        request,
        "achados/objetos/form.html",
        {
            "form": form,
            "titulo": "Editar objeto",
            "objeto": objeto,
        },
    )


def excluir_objeto(request, pk):
    if not request.user.is_authenticated:
        return redirect("achados:login")

    objeto = get_object_or_404(Objeto, pk=pk)

    if request.method == "POST":
        objeto.delete()
        return redirect("achados:index")

    return render(
        request,
        "achados/objetos/excluir.html",
        {"objeto": objeto},
    )


#login/logout
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


#listar
def listar_categorias(request):
    if not request.user.is_authenticated:
        return redirect("achados:login")

    categorias = Categoria.objects.all().order_by("nome")

    return render(
        request,
        "achados/categorias/listar.html",
        {"categorias": categorias},
    )


def cadastrar_categoria(request):
    if not request.user.is_authenticated:
        return redirect("achados:login")

    if request.method == "POST":
        form = CategoriaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("achados:listar_categorias")
    else:
        form = CategoriaForm()

    return render(
        request,
        "achados/categorias/form.html",
        {"form": form, "titulo": "Cadastrar categoria"},
    )


def editar_categoria(request, pk):
    if not request.user.is_authenticated:
        return redirect("achados:login")

    categoria = Categoria.objects.get(pk=pk)

    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=categoria)

        if form.is_valid():
            form.save()
            return redirect("achados:listar_categorias")
    else:
        form = CategoriaForm(instance=categoria)

    return render(
        request,
        "achados/categorias/form.html",
        {"form": form, "titulo": "Editar categoria"},
    )


def excluir_categoria(request, pk):
    if not request.user.is_authenticated:
        return redirect("achados:login")

    categoria = Categoria.objects.get(pk=pk)

    if request.method == "POST":
        categoria.delete()
        return redirect("achados:listar_categorias")

    return render(
        request,
        "achados/categorias/excluir.html",
        {"categoria": categoria},
    )

#local
def listar_locais(request):
    if not request.user.is_authenticated:
        return redirect("achados:login")

    locais = Local.objects.all().order_by("nome")

    return render(
        request,
        "achados/locais/listar.html",
        {"locais": locais},
    )


def cadastrar_local(request):
    if not request.user.is_authenticated:
        return redirect("achados:login")

    if request.method == "POST":
        form = LocalForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("achados:listar_locais")
    else:
        form = LocalForm()

    return render(
        request,
        "achados/locais/form.html",
        {"form": form, "titulo": "Cadastrar local"},
    )


def editar_local(request, pk):
    if not request.user.is_authenticated:
        return redirect("achados:login")

    local = Local.objects.get(pk=pk)

    if request.method == "POST":
        form = LocalForm(request.POST, instance=local)

        if form.is_valid():
            form.save()
            return redirect("achados:listar_locais")
    else:
        form = LocalForm(instance=local)

    return render(
        request,
        "achados/locais/form.html",
        {"form": form, "titulo": "Editar local"},
    )


def excluir_local(request, pk):
    if not request.user.is_authenticated:
        return redirect("achados:login")

    local = Local.objects.get(pk=pk)

    if request.method == "POST":
        local.delete()
        return redirect("achados:listar_locais")

    return render(
        request,
        "achados/locais/excluir.html",
        {"local": local},
    )