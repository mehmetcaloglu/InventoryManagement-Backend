"""
URL configuration for proje_adi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from uygulama_adi.views.products_views import product_list ,product_detail, update_product_detail,delete_product, create_product
from uygulama_adi.views.stocks_views import stock_list,get_stock_detail,get_stock_product_detail,stock_create,stock_update,stock_delete
from uygulama_adi.views.user_views import user_login, user_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('get-products/', get_products, name='get-products'),
    # path('add-product/', add_product, name='add-product'),
    path('update-product/<int:id>/', update_product_detail, name='update-product-detail'),
    path('product-list/', product_list, name='product-list'),
    path('product-detail/<int:id>/', product_detail, name='product-detail'),
    path('product-create/', create_product, name='product-create'),
    path('product-update/<int:id>/', update_product_detail, name='product-update'),
    path('product-delete/<int:id>/', delete_product, name='product-delete'),


    path('stock-list/', stock_list, name='stock-list'),
    path('stock-detail/<int:id>/', get_stock_detail, name='stock-detail'),
    path('stock-create/', stock_create, name='stock-create'),
    path('stock-update/<int:id>/', stock_update, name='stock-update'),
    path('stock-delete/<int:id>/', stock_delete, name='stock-delete'),
    path('get-stock-detail/<int:id>/', get_stock_detail, name='get-stock-detail'),
    path('get-stock-product-detail/<int:id>/', get_stock_product_detail, name='get-stock-product-detail'),

    path('user-login/', user_login, name='user-login'),
    path('user-logout/', user_logout, name='user-logout'),

]
