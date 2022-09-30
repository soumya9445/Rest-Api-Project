from django.contrib import admin
from myapp.models import UserModel,ProductModel

# Register your models here.

@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    fields=('id','user_name','product','user_contact','user_address','user_gender')

@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    fields=('id','product_name','product_price','product_quantity')
