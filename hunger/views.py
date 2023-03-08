from django.shortcuts import render,redirect

from . models import Shop,Items,Ratings,Message,User
from django.db.models import Q
from . shop_form import ShopForm,UserForm,ItemForm,RatingsForm,MyUserCreationForm

from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse
# Create your views here.

# # def home(request):
# #     return render(request,'hunger/home.html')

# def shop(request):
#     return render(request,'hunger/home.html')

@login_required(login_url='login')
def profilepage(request,pk):
    user=User.objects.get(id=pk)
    shops=user.shop_set.all()

    rating=Ratings.objects.all()
    ratings=rating.filter(user_id=pk)
    comments=Message.objects.filter(user_id=pk)


    context={'user':user,'ratings':ratings,'comments':comments,'shops':shops}
    return render(request,'hunger/profile.html',context)

def updateuser(request):
    page="update-user"
    user=request.user
    form=UserForm(instance=user)

    if request.method == 'POST':
        form=UserForm(request.POST,request.FILES ,instance=user)
        if form.is_valid:
            form.save()
            return redirect('profile',pk=user.id)
    
    context={'page':page,'user':user,'form':form}
    return render(request,'hunger/account.html',context)

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    page='login'
    if request.method=='POST':
        username=request.POST.get('username').lower()
        password=request.POST.get('password')
        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request,'user does not exist')

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('profile', pk=user.id)
    
        else:
            messages.error(request,'Username or Password does not exist')
    
    context={'page':page}
    return render(request,'hunger/account.html',context)



def logoutpage(request):
    logout(request)
    return redirect('home')


def registerpage(request):
    page="register"
    form=MyUserCreationForm()
    
    if request.method=='POST':
        form=MyUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username = user.username.lower()
            user.save()
    

            login(request,user)
            return redirect('home')
        else:
             messages.error(request,'An error occured during registration')

    context={'page':page,'form':form}
    return render(request,'hunger/account.html',context)

            
       




def home(request):
    q=request.GET.get('q') if request.GET.get('q')!=None else ''

    shops=Shop.objects.filter(Q(shop_name__contains=q) | Q(location__icontains=q) | Q(description__icontains=q))
    # shops.order_by('shop_name').values()

    # shops=Shop.objects.all()
    shop_count=shops.count()
    
    ratings=Ratings.objects.all()

    # # if request.method=='GET':

    context={'shops':shops,'ratings':ratings,'shop_count':shop_count}

    return render(request,'hunger/home.html',context)



@login_required(login_url='login')
def shop(request,pk):
    shop=Shop.objects.get(id=pk)
    ratings=Ratings.objects.filter(shopname_id=pk)
    ratings_count=ratings.count()

    if ratings.filter(user =request.user).exists():
        userstars="rated"
    else:
        userstars="notrated"

    #     items=shop.items_set.all()
    
    if ratings_count != 0:
        stars=ratings
        a=0
        for star in stars:
            a+=int(star)
        average_ratings=a/ratings_count

    else:
        average_ratings=0

    comments=request.POST.get('comments')
    if comments != None:
        user=request.user
        message=Message.objects.create(
            user=user,
            shop=shop,
            body=request.POST.get('comments')
        )

    comments=shop.message_set.all()

    stars=request.GET.get('stars')
    if stars !=None:
                user=request.user
                rating=Ratings.objects.create(
                user=user,
                shopname=shop,
                stars=request.GET.get('stars')
                )
                return redirect('shop',pk=shop.id)

        

    z=request.GET.get('z')
    if  z != None:
        items=shop.items_set.all()
        item=items.filter(Q(name__icontains=z) )

    else:
        item=shop.items_set.all()

    items_count=item.count()


    # ratings=Ratings.objects.get(shopname_id=pk)

    # rating_count=ratings.count()
    
    context={'shop':shop,'item':item,'comments':comments,'items_count':items_count,
    'ratings_count':ratings_count,'userstars':userstars,
    'average_ratings':average_ratings}

    return render(request,'hunger/shop.html',context)


@login_required(login_url='login')
def createshop(request):
    page="createshop"
    form=ShopForm()

    if request.method=='POST':
        form=ShopForm(request.POST)
        if form.is_valid():
            shop=form.save(commit=False)
            shop.shop_host=request.user
            shop.save()


            # a=str(shop.id)
            # b='shop/'+a
            return redirect('shop',pk=shop.id)


    context={'form':form ,'page':page}

    return render(request,'hunger/shop-form.html',context)



def updateshop(request,pk):
    page="updateshop"
    shop=Shop.objects.get(id=pk)
    form=ShopForm(instance=shop)

    if request.method=='POST':
        form=ShopForm(request.POST,instance=shop)
        if form.is_valid():
            shop.save()
            return redirect('shop',pk=shop.id)


    context={'page':page,'form':form}
    return render(request,'hunger/shop-form.html',context)




def deleteshop(request,pk):
    page="deleteshop"
    shop=Shop.objects.get(id=pk)
    form=ShopForm(instance=shop)

    if request.method=='POST':
        shop.delete()
        return redirect('home')
    
    context={'page':page,'form':form}
    return render(request,'hunger/shop-form.html',context)
    



          #  Items

def createitem(request,pk):
    page="createitem"
    form=ItemForm()
    shop=Shop.objects.get(id=pk)
    

    if request.method=='POST':

        item=Items.objects.create(
        shop=shop,
        name=request.POST.get('name'),
        price=request.POST.get('price'),)
        # a='/'
        # b=str(shops.id)
        # c=a+'shop/'+b

        return redirect('shop',pk=shop.id)
        
    context={'form':form,'page':page}

    return render(request,'hunger/shop-form.html',context)



def updateitem(request,pk):
    page="updateitem"

    item=Items.objects.get(id=pk)
    shop=Shop.objects.get(shop_name=item.shop) 
    # shops=Shop.objects.get(shop_name=shop)
    form=ItemForm(instance=item)

    if request.method=='POST':
        form=ItemForm(request.POST,instance=item)
        if form.is_valid():
            item.save()
            # a='/'
            # b=str(shop.id)
            # c=a+'shop/'+b
            return redirect('shop',pk=shop.id)

    context={'page':page,'form':form}
    return render(request,'hunger/shop-form.html',context)



def deleteitem(request,pk):

    page="deleteitem"

    item=Items.objects.get(id=pk)
    shop=Shop.objects.get(shop_name=item.shop) 
    form=ItemForm(instance=item)

    if request.method=='POST':
        item.delete()
        # a='/'
        # b=str(shop.id)
        # c=a+'shop/'+b
        return redirect('shop',pk=shop.id)
    
    context={'page':page,'form':form}
    return render(request,'hunger/shop-form.html',context)



def deletemessage(request,pk):
    message=Message.objects.get(id=pk)
    shop=Shop.objects.get(shop_name=message.shop) 
    message.delete()
    return redirect(request.META.get('HTTP_REFERER'))



def deleterating(request,pk):
    ratings=Ratings.objects.get(id=pk)
    shop=ratings.shopname
    ratings.delete()

    return redirect('profile', pk=ratings.user.id)


def separateComments(request,pk):
    context={}
    return render(request,'hunger/separate_comment.html',context)

# profile


