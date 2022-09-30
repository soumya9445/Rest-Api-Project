from django.shortcuts import render
from myapp.models import UserModel,ProductModel
from myapp.serializers import UserSerializer,ProductSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.throttling import ScopedRateThrottle
# Create your views here.

class ProductListNCreate(ListCreateAPIView):
    queryset=ProductModel.objects.all()
    serializer_class=ProductSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['product_name','product_price','product_quantity']
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='product'


class ProductRetrieveNUpdateNDelete(RetrieveUpdateDestroyAPIView):
    queryset=ProductModel.objects.all()
    serializer_class=ProductSerializer 
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['product_name','product_price','product_quantity']
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='product'
   

class UserListNCreate(ListCreateAPIView):
    queryset=UserModel.objects.all()
    serializer_class=UserSerializer
    filter_backends=[SearchFilter]
    search_fields=['user_name']
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='user'

class UserRetrieveNUpdateNDelete(RetrieveUpdateDestroyAPIView):
    queryset=UserModel.objects.all()
    serializer_class=UserSerializer   
    filter_backends=[OrderingFilter]
    ordering_fields=['user_name']
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='user' 
    

