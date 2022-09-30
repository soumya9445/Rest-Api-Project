from django.db import models


class ProductModel(models.Model):
    category=(
        ('hp', 'HP'),
        ('dell','DELL'),
        ('lenovo','LENOVO'),
        ('asus','ASUS'),
        ('acer','ACER'),
    )
    product_name=models.CharField(max_length=60,choices=category,unique=True)
    product_price=models.FloatField()
    product_quantity=models.IntegerField()
    def __str__(self):
        return self.product_name

class  UserModel(models.Model):
   
    user_name=models.CharField(max_length=60)
    product=models.ForeignKey(ProductModel,on_delete=models.CASCADE)
    user_contact=models.IntegerField(unique=True)
    user_address=models.TextField()
    user_gender=models.CharField(max_length=50)
    def __str__(self):
        return self.product

    


