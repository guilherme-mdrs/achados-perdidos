from django import forms

from .models import Categoria, Local, Objeto


class ObjetoForm(forms.ModelForm):
    class Meta:
        model = Objeto
        fields = [
            "nome",
            "descricao",
            "categoria",
            "local",
            "status",
            "devolvido_para",
            "matricula_recebedor",
            "foto",
        ]


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = [
            "nome",
            "descricao",
        ]


class LocalForm(forms.ModelForm):
    class Meta:
        model = Local
        fields = [
            "nome",
            "descricao",
        ]