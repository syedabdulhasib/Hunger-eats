from django.forms import ModelForm
from . models import Shop,Items,Ratings,User
from django.contrib.auth.forms import UserCreationForm

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class ShopForm(ModelForm):

    class Meta:
        model =Shop
        fields='__all__'
        exclude=['shop_host','item']

class UserForm(ModelForm):
    
    class Meta:
        model=User
        
        fields=['avatar','username','email','bio']


class ItemForm(ModelForm):
     
    class Meta:
        model=Items

        fields='__all__'
        exclude=['shop']

# class NewUserForm(UserCreationForm):
    
#     email =forms.EmailField(required=True)

#     class Meta:
#         model=User
#         fields=['username','email','password1','password2']

class RatingsForm(ModelForm):

    class Meta:
        model=Ratings
        fields=['stars']

# class ProfileForm(ModelForm):

#     class Meta:
#         model:Photo
#         fields='__all__'




