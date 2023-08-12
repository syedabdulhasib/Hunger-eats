from rest_framework.decorators import api_view
from rest_framework.response import Response
from hunger.models import Shop,Items
from .serializers import ShopSerializer,ItemSerializer

@api_view(['GET'])
def getRoutes(request):
    routes=[
        'GET /api/',
        'GET /api/shops',
        'GET /api/shops/:id',
    ]
    
    return Response(routes) #safe False used to convert the python list into JSON

@api_view(['GET'])
def getShops(request):
    shops=Shop.objects.all()
    shop_serializer=ShopSerializer(shops,many=True)
    return Response(shop_serializer.data)

@api_view(['GET'])
def getShop(request,pk):
    try:
        shop=Shop.objects.get(id=pk)
        shop_serializer=ShopSerializer(shop,many=False)
        return Response(shop_serializer.data)
    except:
        a="sorry the entered shop id not exits"
        return Response(a)

@api_view(['GET'])
def getShopItems(request,pk):
    try:
        shop=Shop.objects.get(id=pk)
        shop_items=shop.items_set.all()
        item_serializer=ItemSerializer(shop_items,many=True)
        return Response(item_serializer.data)
    except:
        a="sorry the entered shop doesn't have any items"
        return Response(a) 

@api_view(['GET'])
def getShopsItems(request):
    try:
        items=Items.objects.all()
        items_serializer=ItemSerializer(items,many=True)
        return Response(items_serializer.data)
    except:
        a="sorry there are no items yet!"
        return Response(a)
