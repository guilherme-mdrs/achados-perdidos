from django.contrib import admin

from .models import Categoria, Local, Objeto


admin.site.register(Categoria)
admin.site.register(Local)
admin.site.register(Objeto)