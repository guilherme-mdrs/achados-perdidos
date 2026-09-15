from apps.commons.api.v1.serializers import BaseSerializer
from apps.achados import models


class CategoriaSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = models.Categoria
        fields = "__all__"


class LocalSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = models.Local
        fields = "__all__"


class ObjetoSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = models.Objeto
        fields = "__all__"

    def get_fields(self):
        fields = super().get_fields()
        fields["usuario"].read_only = True
        fields["usuario"].required = False
        return fields 
        