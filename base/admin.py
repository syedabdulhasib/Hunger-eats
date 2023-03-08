from django.contrib import admin
from . models import Shop,Message,Items,Ratings

# Register your models here.
admin.site.register(Shop)
admin.site.register(Message)
admin.site.register(Items)
admin.site.register(Ratings)