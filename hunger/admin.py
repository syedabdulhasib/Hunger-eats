from django.contrib import admin
from . models import Shop,Message,Items,Ratings,User


admin.site.register(User)
admin.site.register(Shop)
admin.site.register(Message)
admin.site.register(Items)
admin.site.register(Ratings)