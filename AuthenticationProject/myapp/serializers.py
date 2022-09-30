#import imp
#from pyexpat import model
#from tkinter import Widget
from rest_framework import serializers
from myapp.models import UserModel,ProductModel

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=ProductModel
        fields=('id','product_name','product_price','product_quantity')

    def validate_product_price(self,product_price):
        if product_price >= 30000.00 or product_price <= 60000.00:
            return product_price
        else:
            raise serializers.ValidationError('Product Price Starts With 30000.00 And Product Price End With 60000.00 ')        

class UserSerializer(serializers.ModelSerializer):
    #gender=(('male','MALE'),('female','FEMALE'),('others','OTHERS'))
    #user_gender=serializers.ChoiceField(choices=gender,Widget=serializers.Radio)
    class Meta:
        model=UserModel
        fields=('id','user_name','product','user_contact','user_address','user_gender')


    def validate_user_name(self,user_name):
        if user_name.isalpha():
            return user_name
        else:
            raise serializers.ValidationError('Name Must Be Character!!')  


    def validate_user_contact(self,user_contact):
        if len(str(user_contact))== 10:
            return user_contact
        else:
            raise serializers.ValidationError('Contact Number Should Be 10 digit!!')                  