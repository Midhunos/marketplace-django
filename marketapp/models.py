from django.db import models
from django.contrib.auth.models import User
from datetime import datetime





# Create your models here.


class CustomerDetails(models.Model):
     user=models.ForeignKey(User,verbose_name='User',on_delete=models.CASCADE,null=True)
     locality=models.CharField(max_length=150,verbose_name='Location')
     city=models.CharField(max_length=150,verbose_name='City')
     street=models.CharField(max_length=150,verbose_name='Street')
     phono=models.CharField(max_length=15,default='')
     code=models.CharField(max_length=15,verbose_name='Pin Code')

     def __str__(self):
         return self.locality


class Contact(models.Model):
    email=models.EmailField()
    name=models.TextField()
    message=models.TextField()

class Category(models.Model):
     status_choices=[
         
     ('home_decore','home_decore'),
     ('dress','dress'),
     ('footwear','footwear'),
     ('jewellery','jewellery'),
     ('crockeries','crokeries'),
     ('cosmetics','cosmestics'),
     ('gadgets','gadgets'),


     ]
     title=models.CharField(max_length=50,verbose_name="category title")
     slug=models.SlugField(max_length=55,verbose_name="category slug")
     description=models.TextField(blank=True,verbose_name="category description")
     category_img=models.ImageField(upload_to='category',blank=True,verbose_name="category image")
     is_active=models.BooleanField(verbose_name="is active")
     is_featured=models.BooleanField(verbose_name="is featured")
     choice=models.CharField(max_length=15,choices=status_choices)

     class meta:
          verbose_name_plural='categories'
          ordering=('_created_at')

     def __str__ (self):
      return self.title  

class Product(models.Model):
    title=models.CharField(max_length=150,verbose_name='Product Title')
    slug=models.SlugField(max_length=150,verbose_name='product slug')  
    sku=models.CharField(max_length=225,unique='True',verbose_name=" unique product ID (SKU)")
    description=models.TextField(blank="True",null="True",verbose_name="Detail Description")
    product_image=models.ImageField(upload_to="product",blank="True",null="True",verbose_name="Product Image")
    price=models.DecimalField(max_digits=8,decimal_places=2)
    category=models.ForeignKey(Category,verbose_name="Product Category",on_delete=models.CASCADE)
    is_active=models.BooleanField(verbose_name="is active")
    is_featured=models.BooleanField(verbose_name="is featured")
    created_at=models.DateTimeField(auto_now_add=True,verbose_name="created date")
    updated_at=models.DateTimeField(auto_now_add=True,verbose_name="updated date")
    class Meta:
        verbose_name_plural='Products'
        ordering=('-created_at',)
    def __str__(self):
        return self.title  

class Relatedimage(models.Model):
    products=models.ForeignKey(Product,default=None,on_delete=models.CASCADE)
    image=models.FileField(upload_to='related',null=True)

class Cart(models.Model):
    user=models.ForeignKey(User,verbose_name='User',on_delete=models.CASCADE)
    product=models.ForeignKey(Product,verbose_name='Product',on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default='1',verbose_name='quantity')

    def __str__(self):
        return str(self.user)  
    @property
    def total_price(self):
        return self.quantity*self.product.price
    

class Order(models.Model):
       STATUS_CHOICES=[
           ('pending','pending'),
           ('accepted','accepted'),
           ('On the way','On the way'),
           ('deliverd','delivered'),
       ]




       id=models.IntegerField(primary_key=True,editable=False)
       order_id=models.CharField(null=True,max_length=50)
       user=models.ForeignKey(User,verbose_name='User',on_delete=models.CASCADE,null=True,blank=True)
       total=models.FloatField(null=True)
       subtotal=models.FloatField(null=True)
       address=models.ForeignKey(CustomerDetails,verbose_name='shipping addresss',on_delete=models.CASCADE,null=True)
       orderd_date=models.DateTimeField(default=datetime.now,null=True,verbose_name='Date and Time')
       status=models.CharField(choices=STATUS_CHOICES,default='pending',max_length=130)
      





