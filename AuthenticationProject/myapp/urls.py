from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Plistncreate/',views.ProductListNCreate.as_view()),
    path('PRetrieveNUpdateNDelete/<pk>',views.ProductRetrieveNUpdateNDelete.as_view()),
    path('Ulistncreate/',views.UserListNCreate.as_view()),
    path('URetrieveNUpdateNDelete/<pk>',views.UserRetrieveNUpdateNDelete.as_view()),
]