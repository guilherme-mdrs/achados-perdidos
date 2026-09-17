from django.urls import path

from .views import (
    cadastrar_categoria,
    cadastrar_local,
    cadastrar_objeto,
    editar_categoria,
    editar_local,
    excluir_categoria,
    excluir_local,
    index,
    listar_categorias,
    listar_locais,
    login_usuario,
    logout_usuario,
)

app_name = "achados"

urlpatterns = [
    path("", index, name="index"),
    path("cadastrar/", cadastrar_objeto, name="cadastrar"),
    path("login/", login_usuario, name="login"),
    path("sair/", logout_usuario, name="logout"),

    path("categorias/", listar_categorias, name="listar_categorias"),
    path("categorias/cadastrar/", cadastrar_categoria, name="cadastrar_categoria"),
    path("categorias/<int:pk>/editar/", editar_categoria, name="editar_categoria"),
    path("categorias/<int:pk>/excluir/", excluir_categoria, name="excluir_categoria"),

    path("locais/", listar_locais, name="listar_locais"),
    path("locais/cadastrar/", cadastrar_local, name="cadastrar_local"),
    path("locais/<int:pk>/editar/", editar_local, name="editar_local"),
    path("locais/<int:pk>/excluir/", excluir_local, name="excluir_local"),
]