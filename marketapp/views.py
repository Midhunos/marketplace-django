from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .forms import SignupForm,SigninForm,ProductForm,AddressForm
from django.contrib.auth import authenticate,login,logout
from django.conf import settings
from django.core.mail import send_mail
from .models import Contact,Category,Product,Relatedimage,Cart,CustomerDetails,Order
from django.contrib.auth.decorators import login_required
import decimal
from django.db.models import Q


# Create your views here.
def registrations(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.save()
            messages.info(request,'user saved sucessfully')
            return redirect('log')
        else:
            messages.info(request,'invalid')
    else:
        form=SignupForm()
    context={
            'form':form
        }
    return render(request,'registration.html',context)
def log(request):
    if request.method=='POST':
        form=SigninForm(request.POST)
        username=form['username'].value()
        password=form['password'].value()
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.info(request,'login sucessfull')
            return redirect('index')
        else:
            messages.info(request,'invalid')
    else:
        form=SigninForm()
    context={
        'form':form
    }            

    return render(request,'log.html',context)
def index(request):
    categoriespage=Category.objects.filter(is_active=True,is_featured=True)[:6]
    products=Product.objects.filter(is_active=True,is_featured=True)[:8]

    context={
        'categoriespage':categoriespage,
        'products':products,


    }

    return render(request,'index.html',context)
def products(request):
    categoriespage=Category.objects.filter(is_active=True)
    return render(request,'products.html',{'categoriespage':categoriespage})
# def checkout(request):
#     return render(request,'checkout.html')
def furniture(request):
    return render(request,'furniture.html')
def logas(request):
    return render(request,'login.html')
def mail(request):
    if request.method=='POST':
        email=request.POST['email']
        name=request.POST['name']
        mssg=request.POST['msg']
        Contact(email=email,name=name,message=mssg).save()
        send_mail(subject='thankyou',message='thankyou for contacting us',from_email=settings.EMAIL_HOST_USER,recipient_list=[email,],fail_silently=False)
        messages.info(request,'THANKU FOR YOUR RESPONCE')


    return render(request,'mail.html')
def register(request):
    return render(request,'register.html')
def shortcode(request):
    return render(request,'short-codes.html')

def pro(request,slug,):
    category=get_object_or_404(Category,slug=slug)
    products=Product.objects.filter(is_active=True,category=category,)
    categories=Category.objects.filter(is_active=True)
    context={
        'category':category,
        'products':products,
        'categories': categories,


    }
    return render(request,'singletwo.html',context)
def gadgets(request):
    gadg=Category.objects.filter(choice="gadgets")
    context={
        'gadg':gadg,
    }
    return render(request,'single.html',context)
def footwear(request):
    foot=Category.objects.filter(choice="footwear")
    context={
        'foot':foot,
    }
    return render(request,'footwear.html',context)
def jewellery(request):
    jewel=Category.objects.filter(choice="jewellery")
    context={
        'jewel':jewel,
    }
    return render(request,'jewellery.html',context)
def homedecore(request):
    decore=Category.objects.filter(choice="home_decore")
    context={
        'decore':decore,
    }
    return render(request,'home_decore.html',context)
def crockeries(request):
    crock=Category.objects.filter(choice="crockeries")
    context={
        'crock':crock,
    }
    return render(request,'crockeries.html',context)
def cosmetics(request):
    cosmet=Category.objects.filter(choice="cosmetics")
    context={
        'cosmet':cosmet,
    }
    return render(request,'cosmetics.html',context)
def clothings(request):
    cloth=Category.objects.filter(choice="clothings")
    context={
        'cloth':cloth,
    }
    return render(request,'clothings.html',context)
def detailpage(request,slug):
    product=get_object_or_404(Product,slug=slug)
    relatedimages=Relatedimage.objects.filter(products=product.id)

    context={
        'product':product,
        'relatedimages':relatedimages,
    }



    return render(request,'detatil.html',context)
@login_required
def cart(request):
    user=request.user
    cart_products=Cart.objects.filter(user=user)
    amount=decimal.Decimal(0)
    service_amount=decimal.Decimal(10)
    cp=[p for p in Cart.objects.all() if p.user==user]
    if cp:
        for p in cp:
            temp_amount=(p.quantity * p.product.price)
            amount += temp_amount
    context={
        'cart_products':cart_products,
        'amount':amount,
        'service_amount':service_amount,
        'total_amount':amount + service_amount,
    }    
    return render(request,'carts.html',context)    


@login_required
def add_to_cart(request):
    user=request.user
    print(request.user)
    product_id=request.GET.get('prod_id')
    product=get_object_or_404(Product,id=product_id,)
   
    item_already_in_cart=Cart.objects.filter(product=product_id,user=user)
    if item_already_in_cart:
        cp=get_object_or_404(Cart,product=product_id, user=user)
        cp.quantity += 1
        cp.save()
    else:
        Cart(user=user,product=product).save()
        return redirect('cart')   
    return redirect('cart') 

@login_required
def pluscart(request,cart_id):
    if request.method=='GET':
        cp=get_object_or_404(Cart,id=cart_id)
        cp.quantity +=1
        cp.save()
    return redirect('cart')
@login_required
def minuscart(request,cart_id):
    if request.method=='GET':
        cp=get_object_or_404(Cart,id=cart_id)
        if cp.quantity==1:
            cp.delete()
        else:
            cp.quantity-=1
            cp.save()
    return redirect('cart')
def delete(request,cart_id):
    if request.method=='GET':
        cp=get_object_or_404(Cart,id=cart_id)
        cp.delete()
        return redirect('cart')
    
def classified(request):
      context={}
      form=ProductForm(request.POST or None,request.FILES or None)
      if form.is_valid():
          form.save()
      context['form']=form    

   
      return render(request,'vendor/all_classifieds.html',context)     
def sell(request):

    return render(request,'vendor/sellers.html')

@login_required
def userProfiles(request):
    addresses = CustomerDetails.objects.filter(user=request.user)
    print(request.user)
    print(addresses)
    orders = Order.objects.filter(user=request.user).order_by('-user_id')
    context={
           'addresses': addresses,
            'orders': orders
    }
    return render(request, 'profile.html',context)


def adres(request):
    if request.method=='POST':
      form=AddressForm(request.POST)
      if form.is_valid():
         address=form.save(commit=False)
         address.save()
         messages.info(request,'Address saved sucessfully')
         return redirect('userProfiles') 
      else:
          messages.info(request,'invalid')
    else:
        form=AddressForm()
        context={
            'form':form
        }    
          
     
    return render(request,'order.html',context)
@login_required
def checkout(request):
    # user=request.user
    # address_id=request.GET.get('address')
    # address=get_object_or_404(CustomerDetails,id=address_id)
    # cart=Cart.objects.filter(user=user)
    # for c in cart:
    #     Order(user=user,address=address,product=c.product,quantity=c.quantity).save()
    #     c.delete()
    return render(request,'checkouts.html')

@login_required
def buy(request):
    all_orders=Order.objects.get(user=request.user).order_by('-ordered_date')
    return render(request,'checkouts.html',{'orders':all_orders})




def search(request):
    q=request.GET.get('q','')
    data=Product.objects.filter(title__icontains=q).order_by('-id')
    return render(request,'search.html',{'data':data})
def logoutpage(request):
    # print('logged out')
   logout(request)
   messages.info(request,'login failed')
   return redirect('/') 