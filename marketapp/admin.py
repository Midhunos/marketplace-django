from django.contrib import admin
from .models import Contact,Category,Product,Relatedimage,Order


# Register your models here.
class categoryAdmin(admin.ModelAdmin):
      list_display=('title','slug','category_img','is_featured','is_active')
      list_editable=('slug','is_active','is_featured')
      list_filter=('is_active','is_featured')
      search_fields=('title','description')
      prepopulated_fields={"slug":("title",)}

class RelatedimageAdmin(admin.StackedInline):
      model=Relatedimage

class ProductAdmin(admin.ModelAdmin):
      list_display=('title','slug','product_image','is_active','is_featured','description')
      list_editable=('slug','is_active','is_featured')
      list_filter=('is_active','is_featured')
      search_fields=('title','description','price',)
      prepopulated_fields={"slug":("title",)}
      inlines=[RelatedimageAdmin]
class CustomerAdmin(admin.ModelAdmin):
      list_display=('address','order_id','total','orderd_date','status',)     

    

admin.site.register(Contact)
admin.site.register(Category,categoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Order,CustomerAdmin)

