"""library_practice1 URL Configuration

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
from app1 import views
from django.urls import path, include, re_path # Add django-debug-toolbar’s URLs to your project’s URLconf
# from django.conf.urls import url #---> django 4.0 cversion pasan url import nhi karta yet --- we have re_path

from app1.views import *
# from app1 import views #--> recommend to use this 

print('in uels.py ------')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.homepage, name='home'),
    path('show-all-books/', views.show_all_books, name='show_all_books'),
    path('edit/<int:id>/', views.edit_data, name='edit'),
    path('delete/<int:id>/', views.delete_data, name='delete'),
    path('form-view/', views.form_view, name='form_view'), # for 1st form 
    path('book-model-view/', views.book_model_view, name='book_model_view'),
    path('test-form-view/', views.test_form_view, name='test_form_view'), # for test form only 


    # class bases view practice
    path('cbv-home/', views.Home.as_view(), name='home'),


    path('product-view/', views.product_view, name='product_view'),
    path('login-prack/', views.user_login, name='user_login'),
]


# urlpatterns += [
#     # ...
#     path('__debug__/', include('debug_toolbar.urls')),
# ]


# http://127.0.0.1:8000/cbv-home/


urlpatterns += [
    re_path(r'^aaa$', views.view_a, name='view_a'),
    re_path(r'^bbb$', views.view_b, name='view_b'),
    re_path(r'^ccc$', views.view_c, name='view_c'),
    re_path(r'^ddd$', views.view_d, name='view_d'),
]