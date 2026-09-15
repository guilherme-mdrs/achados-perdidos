from rest_framework.routers import DefaultRouter

from apps.achados.api.v1 import viewsets


achados_router = DefaultRouter()

achados_router.register(
    r"categorias",
    viewsets.CategoriaViewSet,
    basename="categoria",
)

achados_router.register(
    r"locais",
    viewsets.LocalViewSet,
    basename="local",
)

achados_router.register(
    r"objetos",
    viewsets.ObjetoViewSet,
    basename="objeto",
)