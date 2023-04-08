from django.urls import path
from .import views


urlpatterns=[

    path('',views.log,name='log'),
    path('registrations',views.registrations,name='registrations'),
    
    path('index',views.index,name='index'),
    path('products',views.products,name='products'),
    
   
   
    path('logas/',views.login,name='login'),
    path('add_to_cart/',views.add_to_cart,name='add_to_cart'),
    path('cart/',views.cart,name='cart'),
    path('pluscart/<int:cart_id>/',views.pluscart,name='pluscart'),
    path('minuscart/<int:cart_id>/',views.minuscart,name='minuscart'),
    path('delete/<int:cart_id>/',views.delete,name='delete'),
    path('furniture',views.furniture,name='furniture'),
    path('mail',views.mail,name='mail'),
    path('register',views.register,name='register'),
    # path('shortcode',views.shortcode,name='shortcode'),
    path('<slug:slug>',views.pro,name='pro'),
    path('footwear',views.footwear,name='footwear'),
    path('gadgets/',views.gadgets,name='gadgets'),
    path('jewellery/',views.jewellery,name='jewellery'),
    path('homedecore/',views.homedecore,name='homedecore'),
    path('crockeries/',views.crockeries,name='crockeries'),
    path('cosmetics/',views.cosmetics,name='cosmetics'),
    path('clothings/',views.clothings,name='clothings'),
    path('product/<slug:slug>/',views.detailpage,name='detailpage'),
   
    path('sell/',views.sell,name='vendor/sell'),
    path('classified/',views.classified,name='vendor/classified'),
   
    path('adres/',views.adres,name='adres'),
   
    path('buy/',views.buy,name='buy'),


    path('profile/',views.userProfiles,name='userProfiles'),
    
    path('checkout/',views.checkout,name='checkout'),
    path('search/',views.search,name='search'),
    path('logoutpage/',views.logoutpage,name='logoutpage'),
    

  




   
   
 

    


    


]