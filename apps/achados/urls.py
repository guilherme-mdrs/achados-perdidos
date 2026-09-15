from django.urls import path

from .views import (
    cadastrar_objeto,
    index,
    login_usuario,
    logout_usuario,
)


app_name = "achados"


urlpatterns = [
    path("", index, name="index"),
    path("cadastrar/", cadastrar_objeto, name="cadastrar"),
    path("login/", login_usuario, name="login"),
    path("sair/", logout_usuario, name="logout"),
]

