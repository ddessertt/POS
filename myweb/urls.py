"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from POS import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.Home, name='index'),
    path('management/', views.management, name='management'),
    path('add_product/', views.add_product, name='add'),
    path('add_type/', views.add_type, name='add_type'),
    path('edit_product/<int:product_id>/', views.product_edit, name='product_edit'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('', views.my_login, name='login'),
    path('logout/', views.my_logout, name='logout'),
]
