from rest_framework.serializers import ModelSerializer
from hunger.models import Shop

class ShopSerializer(ModelSerializer):
    class Meta:
        model=Shop
        fields='__all__'