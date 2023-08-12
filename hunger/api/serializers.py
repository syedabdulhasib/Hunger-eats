from rest_framework.serializers import ModelSerializer
from hunger.models import Shop,Items

class ShopSerializer(ModelSerializer):
    class Meta:
        model=Shop
        fields='__all__'

class ItemSerializer(ModelSerializer):
    class Meta:
        model=Items
        fields='__all__'
