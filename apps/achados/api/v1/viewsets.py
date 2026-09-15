from apps.commons.api.v1.viewsets import BaseModelApiViewSet
from rest_framework.exceptions import PermissionDenied
from apps.achados import models


class CategoriaViewSet(BaseModelApiViewSet):
    model = models.Categoria


class LocalViewSet(BaseModelApiViewSet):
    model = models.Local


class ObjetoViewSet(BaseModelApiViewSet):
    model = models.Objeto

    def get_queryset(self):
        queryset = super().get_queryset()

        return queryset.select_related(
            "usuario",
            "categoria",
            "local",
        ).order_by("-created_at")

    def perform_create(self, serializer):
        serializer.validated_data["usuario"] = self.request.user
        super().perform_create(serializer)

    def perform_update(self, serializer):
        objeto = serializer.instance

        if objeto.usuario != self.request.user and not self.request.user.is_staff:
            raise PermissionDenied(
                "Você não tem permissão para alterar este objeto."
            )

        super().perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.usuario != self.request.user and not self.request.user.is_staff:
            raise PermissionDenied(
                "Você não tem permissão para excluir este objeto."
            )

        super().perform_destroy(instance)
